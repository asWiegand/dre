from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from . import models, forms
from django.urls import reverse_lazy
from .models import Bank

class BankCreate(CreateView):
    model = models.Bank
    template_name = 'bank_list.html'
    form_class = forms.BankForm
    success_url = reverse_lazy('bank_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['banks'] = Bank.objects.all()  # adiciona todos os bancos no contexto
        return context

class BankDeleteView(DeleteView):
    model = models.Bank
    template_name = 'bank_list.html'
    success_url = reverse_lazy('bank_list')

class BankUpdateView(UpdateView):
    model = models.Bank
    template_name = 'bank_list.html'
    form_class = forms.BankForm
    success_url = reverse_lazy('bank_list')