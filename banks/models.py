from django.db import models

class Bank(models.Model):
    bank_name = models.CharField(max_length=25)
    balance = models.DecimalField(max_digits=20, decimal_places=2, default=0)

    class Meta:
        ordering = ['bank_name']
    
    def __str__(self):
        return self.bank_name