from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, UpdateView
from . import models, forms
from django.urls import reverse_lazy
from .models import Supplier

class SupplierCreate(CreateView):
    model = models.Supplier
    template_name = 'supplier_list.html'
    form_class = forms.SupplierForm
    success_url = reverse_lazy('supplier_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['suppliers'] = Supplier.objects.all()  # adiciona todos os bancos no contexto
        return context

class SupplierDeleteView(DeleteView):
    model = models.Supplier
    template_name = 'supplier_list.html'
    success_url = reverse_lazy('supplier_list')

class SupplierUpdateView(UpdateView):
    model = models.Supplier
    template_name = 'supplier_list.html'
    form_class = forms.SupplierForm
    success_url = reverse_lazy('supplier_list')