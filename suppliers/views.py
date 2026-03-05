from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from . import models, forms
from django.urls import reverse_lazy
from .models import Supplier

class SupplierListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'suppliers.view_supplier'
    model = models.Supplier
    template_name = 'supplier_list.html'
    context_object_name = 'suppliers'

class SupplierCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'suppliers.add_supplier'
    model = models.Supplier
    template_name = 'supplier_form.html'
    form_class = forms.SupplierForm
    success_url = reverse_lazy('supplier_list')

class SupplierUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'suppliers.change_supplier'
    model = models.Supplier
    template_name = 'supplier_form.html'
    form_class = forms.SupplierForm
    success_url = reverse_lazy('supplier_list')

class SupplierDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'suppliers.delete_supplier'
    model = models.Supplier
    template_name = 'supplier_confirm_delete.html'
    success_url = reverse_lazy('supplier_list')
