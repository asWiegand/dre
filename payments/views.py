from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Payment
from . import forms

class PaymentListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'payments.view_payment'
    model = Payment
    template_name = 'payment_list.html'
    context_object_name = 'payments'

class CreatePaymentView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'payments.add_payment'
    model = Payment
    template_name = 'payment_form.html'
    form_class = forms.PaymentForm
    success_url = reverse_lazy('payment_list')

class PaymentUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'payments.change_payment'
    model = Payment
    template_name = 'payment_form.html'
    form_class = forms.PaymentForm
    success_url = reverse_lazy('payment_list')

class PaymentDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'payments.delete_payment'
    model = Payment
    template_name = 'payment_confirm_delete.html'
    success_url = reverse_lazy('payment_list')
