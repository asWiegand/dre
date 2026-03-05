from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from . import models, forms
from django.urls import reverse_lazy
from .models import Bank

class BankListView(LoginRequiredMixin, ListView):
    model = models.Bank
    template_name = 'bank_list.html'
    context_object_name = 'banks'

class BankCreateView(LoginRequiredMixin, CreateView):
    model = models.Bank
    template_name = 'bank_form.html'
    form_class = forms.BankForm
    success_url = reverse_lazy('bank_list')

class BankDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Bank
    template_name = 'bank_confirm_delete.html'
    success_url = reverse_lazy('bank_list')

class BankUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Bank
    template_name = 'bank_form.html'
    form_class = forms.BankForm
    success_url = reverse_lazy('bank_list')
