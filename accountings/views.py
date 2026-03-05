from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from . import models, forms
from django.urls import reverse_lazy
from .models import Accounting

class AccountingListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'accountings.view_accounting'
    model = models.Accounting
    template_name = 'accounting_list.html'
    context_object_name = 'accountings'

class AccountingCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'accountings.add_accounting'
    model = models.Accounting
    template_name = 'accounting_form.html'
    form_class = forms.AccountingForm
    success_url = reverse_lazy('accounting_list')

class AccountingUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'accountings.change_accounting'
    model = models.Accounting
    template_name = 'accounting_form.html'
    form_class = forms.AccountingForm
    success_url = reverse_lazy('accounting_list')

class AccountingDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'accountings.delete_accounting'
    model = models.Accounting
    template_name = 'accounting_confirm_delete.html'
    success_url = reverse_lazy('accounting_list')
