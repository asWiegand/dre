from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from . import models, forms
from django.urls import reverse_lazy
from .models import Accounting

class AccountingCreateView(CreateView):
    model = models.Accounting
    template_name = 'accounting_list.html'
    form_class = forms.AccountingForm
    success_url = reverse_lazy('accounting_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['accountings'] = Accounting.objects.all()  # adiciona todos os bancos no contexto
        return context

class AccountingDeleteView(DeleteView):
    model = models.Accounting
    template_name = 'accounting_list.html'
    success_url = reverse_lazy('accounting_list')