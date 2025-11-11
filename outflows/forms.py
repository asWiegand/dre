from django import forms
from .models import Outflow, Accounting

class OutflowForm(forms.ModelForm):
    installments = forms.IntegerField(
        min_value=1,
        initial=1,
        help_text="Quantidade de parcelas (1 = à vista)",
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Outflow
        fields = ['created_date', 'expire_date', 'supplier', 'accounting', 'payment_method', 'title', 'value']

        widgets = {
            'created_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'expire_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'supplier': forms.Select(attrs={'class': 'form-control'}),
            'accounting': forms.Select(attrs={'class': 'form-control'}),
            'payment_method': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título da despesa'}),
            'value': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'placeholder': '0.00'}),
        }

        labels = {
            'created_date': 'Data de Criação',
            'expire_date': 'Data de Vencimento',
            'supplier': 'Fornecedor',
            'accounting': 'Plano de Contas',
            'payment_method': 'Forma de Pagamento',
            'title': 'Título',
            'value': 'Valor',
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['accounting'].queryset = Accounting.objects.filter(type='S')


class OutflowUpdateForm(forms.ModelForm):
    class Meta:
        model = Outflow
        # Inclua todos os campos que podem ser editados, exceto 'installments'
        fields = ['created_date', 'expire_date', 'supplier', 'accounting', 'payment_method', 'value']
        widgets = {
            'created_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'expire_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'supplier': forms.Select(attrs={'class': 'form-control'}),
            'accounting': forms.Select(attrs={'class': 'form-control'}),
            'payment_method': forms.Select(attrs={'class': 'form-control'}),
            'value': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
        }
        labels = {
            'created_date': 'Data de Criação',
            'expire_date': 'Data de Vencimento',
            'supplier': 'Fornecedor',
            'accounting': 'Plano de Contas',
            'payment_method': 'Forma de Pagamento',
            'value': 'Valor',
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['accounting'].queryset = Accounting.objects.filter(type='S')