from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Payment
from . import forms

class PaymentListView(LoginRequiredMixin, ListView):
    model = Payment
    template_name = 'payment_list.html'
    context_object_name = 'payments'

class CreatePaymentView(LoginRequiredMixin, CreateView):
    model = Payment
    template_name = 'payment_form.html'
    form_class = forms.PaymentForm
    success_url = reverse_lazy('payment_list')

class PaymentUpdateView(LoginRequiredMixin, UpdateView):
    model = Payment
    template_name = 'payment_form.html'
    form_class = forms.PaymentForm
    success_url = reverse_lazy('payment_list')

class PaymentDeleteView(LoginRequiredMixin, DeleteView):
    model = Payment
    template_name = 'payment_confirm_delete.html'
    success_url = reverse_lazy('payment_list')
