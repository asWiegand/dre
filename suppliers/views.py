from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from . import models, forms
from django.urls import reverse_lazy
from .models import Supplier

class SupplierListView(LoginRequiredMixin, ListView):
    model = models.Supplier
    template_name = 'supplier_list.html'
    context_object_name = 'suppliers'

class SupplierCreateView(LoginRequiredMixin, CreateView):
    model = models.Supplier
    template_name = 'supplier_form.html'
    form_class = forms.SupplierForm
    success_url = reverse_lazy('supplier_list')

class SupplierUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Supplier
    template_name = 'supplier_form.html'
    form_class = forms.SupplierForm
    success_url = reverse_lazy('supplier_list')

class SupplierDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Supplier
    template_name = 'supplier_confirm_delete.html'
    success_url = reverse_lazy('supplier_list')
