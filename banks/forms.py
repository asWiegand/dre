from django import forms
from . import models


class BankForm(forms.ModelForm):

    class Meta:
        model = models.Bank
        fields = ['bank_name']
        widgets = {
            'bank_name': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'bank_name': 'Nome do Banco',
        }