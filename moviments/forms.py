from django import forms
from . import models


class MovimentForm(forms.ModelForm):

    class Meta:
        model = models.Moviment
        fields = ['moviment_date', 'bank_id', 'accounting', 'value', 'description']
        widgets = {
            'moviment_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'bank_id': forms.Select(attrs={'class': 'form-control'}),
            'accounting': forms.Select(attrs={'class': 'form-control'}),
            'value': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            
        }
        labels = {
            'moviment_date': 'Data',
            'bank_id': 'Banco',
            'accounting': 'Plano de Contas',
            'description': 'Descrição',
            'value': 'Valor',
        }