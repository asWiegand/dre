from django import forms
from .models import Supplier


class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['cnpj_cpf', 'company_name', 'fantasy_name', 'city', 'address', 'phone', 'email']
        widgets = {
            'cnpj_cpf': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'XXX.XXX.XXX-XX ou XX.XXX.XXX/XXXX-XX'}),
            'company_name': forms.TextInput(attrs={'class': 'form-control'}),
            'fantasy_name': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(XX) XXXXX-XXXX'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'exemplo@email.com'}),
        }
        labels = {
            'cnpj_cpf': 'CNPJ/CPF',
            'company_name': 'Razão Social',
            'fantasy_name': 'Nome Fantasia',
            'city': 'Cidade',
            'address': 'Endereço',
            'phone': 'Telefone',
            'email': 'E-mail',
        }
