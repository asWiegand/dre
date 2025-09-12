from django import forms
from . import models


class AccountingForm(forms.ModelForm):

    class Meta:
        model = models.Accounting
        fields = ['acc_name', 'type']
        widgets = {
            'acc_name': forms.TextInput(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-control'}),
                      
        }
        labels = {
            'acc_name': 'Nome',
            'type': 'Tipo',
        }