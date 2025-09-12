from django.views.generic import CreateView, DetailView, DeleteView, UpdateView
from django.shortcuts import redirect, get_object_or_404, render
from .models import Outflow, Supplier, Accounting, Payment
from moviments.models import Moviment
from banks.models import Bank
from .forms import OutflowForm, OutflowUpdateForm
from dateutil.relativedelta import relativedelta
from decimal import Decimal, ROUND_HALF_UP
from . import models, forms
from django.urls import reverse_lazy
from django.db.models import Sum


class CreateOutflowView(CreateView):
    model = Outflow
    form_class = OutflowForm
    template_name = 'outflow_list.html'  # Ajuste para seu template
    success_url = reverse_lazy('outflow_list')  # Ajuste para sua URL de listagem


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['outflows'] = Outflow.objects.all()  # adiciona todos os bancos no contexto
        context['suppliers'] = Supplier.objects.all()
        context['accountings'] = Accounting.objects.all()
        context['payments'] = Payment.objects.all()
        context['banks'] = Bank.objects.all()
        return context

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

        outflows = []
        soma = Decimal('0.00')

        for i in range(installments):
            if i == installments - 1:
                valor_final = total_value - soma
            else:
                valor_final = parcela_valor
                soma += parcela_valor

            outflow = Outflow(
                created_date=created_date,
                expire_date=expire_date + relativedelta(months=i),
                supplier=supplier,
                accounting=accounting,
                payment_method=payment_method,
                title=f"{title} ({i+1}/{installments})" if installments > 1 else title,
                value=valor_final
            )
            outflows.append(outflow)

        Outflow.objects.bulk_create(outflows)

        return redirect(self.success_url)


class OutflowDeleteView(DeleteView):
    model = models.Outflow
    template_name = 'outflow_list.html'
    success_url = reverse_lazy('outflow_list')

class OutflowDetailView(DetailView):
    model = models.Outflow
    template_name = 'outflow_detail.html'

class OutflowUpdateView(UpdateView):
    model = models.Outflow
    template_name = 'outflow_list.html'
    form_class = forms.OutflowUpdateForm
    success_url = reverse_lazy('outflow_list')

def pay_outflow(request, pk):
    outflow = get_object_or_404(Outflow, pk=pk)

    if request.method == 'POST':
        payment_date = request.POST.get('payment_date')
        bank_id = request.POST.get('bank_id')

        if not payment_date or not bank_id:
            return redirect('outflow_list')

        # Atualiza a conta como paga
        outflow.status = 'PG'
        outflow.payment_date = payment_date
        outflow.save()

        # Cria a movimentação no banco
        bank = get_object_or_404(Bank, pk=bank_id)

        Moviment.objects.create(
            moviment_date=payment_date,
            bank_id=bank,
            accounting=outflow.accounting,
            value=Decimal(outflow.value),  # Saída de dinheiro
            description=f"Pagamento: {outflow.title}"
        )

        return redirect('outflow_list')

    return redirect('outflow_list')


def outflow_report(request):
    # Pega parâmetros de filtro
    month = request.GET.get('month')
    year = request.GET.get('year')

    # Obtém lista de anos disponíveis
    years_choices = Outflow.objects.dates('expire_date', 'year', order='DESC')
    month_choices = [
        ('01', 'Janeiro'), ('02', 'Fevereiro'), ('03', 'Março'),
        ('04', 'Abril'), ('05', 'Maio'), ('06', 'Junho'),
        ('07', 'Julho'), ('08', 'Agosto'), ('09', 'Setembro'),
        ('10', 'Outubro'), ('11', 'Novembro'), ('12', 'Dezembro')
    ]

    # Filtragem base
    outflows = Outflow.objects.filter(status='NP')

    if year:
        outflows = outflows.filter(expire_date__year=year)
    if month:
        outflows = outflows.filter(expire_date__month=month)

    # Agrupamento por status
    total_np = outflows.filter(status='NP').aggregate(total=Sum('value'))['total'] or 0

    return render(request, 'outflow_report.html', {
        'outflows': outflows,
        'total_np': total_np,
        'month_choices': month_choices,
        'years_choices': years_choices,
        'month': month,
        'year': year
    })