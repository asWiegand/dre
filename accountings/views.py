from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from . import models, forms
from django.urls import reverse_lazy
from .models import Accounting

class AccountingListView(LoginRequiredMixin, ListView):
    model = models.Accounting
    template_name = 'accounting_list.html'
    context_object_name = 'accountings'

class AccountingCreateView(LoginRequiredMixin, CreateView):
    model = models.Accounting
    template_name = 'accounting_form.html'
    form_class = forms.AccountingForm
    success_url = reverse_lazy('accounting_list')

class AccountingUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Accounting
    template_name = 'accounting_form.html'
    form_class = forms.AccountingForm
    success_url = reverse_lazy('accounting_list')

class AccountingDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Accounting
    template_name = 'accounting_confirm_delete.html'
    success_url = reverse_lazy('accounting_list')
