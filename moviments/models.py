from django.db import models
from accountings.models import Accounting
from banks.models import Bank


class Moviment(models.Model):
    moviment_date = models.DateField()
    bank_id = models.ForeignKey(Bank, on_delete=models.PROTECT, related_name='moviments')
    accounting = models.ForeignKey(Accounting, on_delete=models.PROTECT, related_name='moviments')
    value = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.created_at