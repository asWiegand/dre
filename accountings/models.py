from django.db import models

class Accounting(models.Model):
    INFLOW = "E"
    OUTFLOW = "S"
    TYPE_CHOICES = [(INFLOW, 'Entrada'), (OUTFLOW, 'Saida'),]

    acc_name = models.CharField(max_length=30)
    type = models.CharField(max_length=1, choices=TYPE_CHOICES)


    class Meta:
        ordering = ['acc_name']
    
    def __str__(self):
        return self.acc_name