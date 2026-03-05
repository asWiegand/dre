from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from . import models, forms
from django.urls import reverse_lazy
from .models import Bank

class BankListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'banks.view_bank'
    model = models.Bank
    template_name = 'bank_list.html'
    context_object_name = 'banks'

class BankCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'banks.add_bank'
    model = models.Bank
    template_name = 'bank_form.html'
    form_class = forms.BankForm
    success_url = reverse_lazy('bank_list')

class BankDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'banks.delete_bank'
    model = models.Bank
    template_name = 'bank_confirm_delete.html'
    success_url = reverse_lazy('bank_list')

class BankUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'banks.change_bank'
    model = models.Bank
    template_name = 'bank_form.html'
    form_class = forms.BankForm
    success_url = reverse_lazy('bank_list')
