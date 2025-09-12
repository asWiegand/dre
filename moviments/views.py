from django.shortcuts import render, redirect
from django.views.generic import ListView, UpdateView, DeleteView, DetailView
from . import models, forms
from django.urls import reverse_lazy
from .models import Moviment, Bank, Accounting
from datetime import datetime
from .forms import MovimentForm

class MovimentListView(ListView):
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
        context['form'] = MovimentForm()
        context['banks'] = Bank.objects.all()
        context['accountings'] = Accounting.objects.all()
        context['field'] = self.request.GET.get('field', '')
        return context

    def post(self, request, *args, **kwargs):
        form = MovimentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('moviment_list')
        else:
            context = self.get_context_data()
            context['form'] = form
            return render(request, self.template_name, context)
        
class MovimentDeleteView(DeleteView):
    model = models.Moviment
    template_name = 'moviment_list.html'
    success_url = reverse_lazy('moviment_list')

class MovimentUpdateView(UpdateView):
    model = models.Moviment
    template_name = 'moviment_list.html'
    form_class = forms.MovimentForm
    success_url = reverse_lazy('moviment_list')

class MovimentDetailView(DetailView):
    model = models.Moviment
    template_name = 'moviment_list.html'

