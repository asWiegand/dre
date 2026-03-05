from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404, render
from .models import Supplier, Accounting, Payment, Inflow
from moviments.models import Moviment
from banks.models import Bank
from .forms import InflowForm, InflowUpdateForm
from dateutil.relativedelta import relativedelta
from decimal import Decimal, ROUND_HALF_UP
from . import models, forms
from django.urls import reverse_lazy
from django.db.models import Sum

class InflowListView(LoginRequiredMixin, ListView):
    model = Inflow
    template_name = 'inflow_list.html'
    context_object_name = 'inflows'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['banks'] = Bank.objects.all()
        return context

class CreateInflowView(LoginRequiredMixin, CreateView):
    model = Inflow
    form_class = InflowForm
    template_name = 'inflow_form.html'
    success_url = reverse_lazy('inflow_list')

    def form_valid(self, form):
        created_date = form.cleaned_data['created_date']
        expire_date = form.cleaned_data['expire_date']
        supplier = form.cleaned_data['supplier']
        accounting = form.cleaned_data['accounting']
        payment_method = form.cleaned_data['payment_method']
        title = form.cleaned_data['title']
        total_value = form.cleaned_data['value']
        installments = form.cleaned_data['installments']

        # Calcula valor da parcela com arredondamento
        parcela_valor = (total_value / installments).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

        inflows = []
        soma = Decimal('0.00')

        for i in range(installments):
            if i == installments - 1:
                valor_final = total_value - soma
            else:
                valor_final = parcela_valor
                soma += parcela_valor

            inflow = Inflow(
                created_date=created_date,
                expire_date=expire_date + relativedelta(months=i),
                supplier=supplier,
                accounting=accounting,
                payment_method=payment_method,
                title=f"{title} ({i+1}/{installments})" if installments > 1 else title,
                value=valor_final
            )
            inflows.append(inflow)

        Inflow.objects.bulk_create(inflows)

        return redirect(self.success_url)

class InflowDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Inflow
    template_name = 'inflow_confirm_delete.html'
    success_url = reverse_lazy('inflow_list')

class InflowDetailView(LoginRequiredMixin, DetailView):
    model = models.Inflow
    template_name = 'inflow_detail.html'

class InflowUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Inflow
    template_name = 'inflow_form.html'
    form_class = forms.InflowUpdateForm
    success_url = reverse_lazy('inflow_list')


@login_required
def pay_inflow(request, pk):
    inflow = get_object_or_404(Inflow, pk=pk)

    if request.method == 'POST':
        payment_date = request.POST.get('payment_date')
        bank_id = request.POST.get('bank_id')

        if not payment_date or not bank_id:
            return redirect('inflow_list')

        # Atualiza a conta como paga
        inflow.status = 'PG'
        inflow.payment_date = payment_date
        inflow.save()

        # Cria a movimentação no banco
        bank = get_object_or_404(Bank, pk=bank_id)

        Moviment.objects.create(
            moviment_date=payment_date,
            bank_id=bank,
            accounting=inflow.accounting,
            value=Decimal(inflow.value),  # Saída de dinheiro
            description=f"Pagamento: {inflow.title}"
        )

        return redirect('inflow_list')

    return redirect('inflow_list')


@login_required
def inflow_report(request):
    # Pega parâmetros de filtro
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    # Filtragem base
    inflows = Inflow.objects.filter(status='NP')

    if start_date:
        inflows = inflows.filter(expire_date__gte=start_date)
    if end_date:
        inflows = inflows.filter(expire_date__lte=end_date)

    # Agrupamento por status
    total_np = inflows.filter(status='NP').aggregate(total=Sum('value'))['total'] or 0

    return render(request, 'inflow_report.html', {
        'inflows': inflows,
        'total_np': total_np,
        'start_date': start_date,
        'end_date': end_date
    })