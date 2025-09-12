from django.db import models
from django.core.exceptions import ValidationError
from validate_docbr import CPF, CNPJ

def validate_cpf_cnpj(value):
    cpf = CPF()
    cnpj = CNPJ()
    
    if not (cpf.validate(value) or cnpj.validate(value)):
        raise ValidationError('CPF ou CNPJ inválido.')

class Supplier(models.Model):
    cnpj_cpf = models.CharField(
        max_length=18,
        unique=True,
        validators=[validate_cpf_cnpj],
        verbose_name="CNPJ ou CPF",
        blank=True
    )
    company_name = models.CharField(max_length=100, blank=False, null=False)
    fantasy_name = models.CharField(max_length=100, blank=True, default='')
    city = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=100, blank=True)
    phone = models.CharField(blank=True)
    email = models.EmailField(blank=True)

    def __str__(self):
            return self.company_name