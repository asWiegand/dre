from django.shortcuts import render, redirect
from django.views.generic import ListView, UpdateView, DeleteView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from . import models, forms
from django.urls import reverse_lazy
from .models import Moviment, Bank, Accounting
from datetime import datetime
from .forms import MovimentForm

class MovimentListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'moviments.view_moviment'
    model = Moviment
    template_name = "moviment_list.html"
    context_object_name = "moviments"

    def get_queryset(self):
        queryset = super().get_queryset()
        field = self.request.GET.get('field')
        query = self.request.GET.get('query')

        if field and query:
            if field == 'description':
                queryset = queryset.filter(description__icontains=query)
            elif field == 'value':
                try:
                    value = float(query.replace(',', '.'))
                    queryset = queryset.filter(value=value)
                except ValueError:
                    queryset = queryset.none()
            elif field == 'moviment_date':
                try:
                    date_obj = datetime.strptime(query, '%Y-%m-%d').date()
                    queryset = queryset.filter(moviment_date=date_obj)
                except ValueError:
                    queryset = queryset.none()

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # O formulário não é mais necessário aqui, mas estamos passando os filtros
        context['field'] = self.request.GET.get('field', '')
        return context

class MovimentCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'moviments.add_moviment'
    model = models.Moviment
    template_name = 'moviment_form.html'
    form_class = forms.MovimentForm
    success_url = reverse_lazy('moviment_list')

class MovimentUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'moviments.change_moviment'
    model = models.Moviment
    template_name = 'moviment_form.html'
    form_class = forms.MovimentForm
    success_url = reverse_lazy('moviment_list')

class MovimentDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'moviments.delete_moviment'
    model = models.Moviment
    template_name = 'moviment_confirm_delete.html'
    success_url = reverse_lazy('moviment_list')

class MovimentDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    permission_required = 'moviments.view_moviment'
    model = models.Moviment
    template_name = 'moviment_list.html'  # Pode ser desnecessário ou separado no futuro

