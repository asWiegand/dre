from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Payment
from . import models, forms
from django.urls import reverse_lazy


class CreatePaymentView(CreateView):
    model = models.Payment
    template_name = 'payment_list.html'
    form_class = forms.PaymentForm
    success_url = reverse_lazy('payment_list')
    queryset = Payment.objects.all()  # Adiciona um queryset padrão

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['payments'] = Payment.objects.all()  # adiciona todos os bancos no contexto
        return context