from django.db import models
from accountings.models import Accounting
from suppliers.models import Supplier
from payments.models import Payment
from django.utils import timezone


class Outflow(models.Model):
    created_date = models.DateField()
    expire_date = models.DateField()
    supplier = models.ForeignKey(Supplier, on_delete=models.PROTECT, related_name='outflows')
    accounting = models.ForeignKey(Accounting, on_delete=models.PROTECT, related_name='outflows')
    payment_method = models.ForeignKey(Payment, on_delete=models.PROTECT, related_name='outflows')
    title = models.CharField(max_length=15)
    status = models.CharField(max_length=2, default='NP')
    value = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    payment_date = models.DateField(blank=True, null=True)

    @property
    def is_expired(self):
        return self.expire_date < timezone.localdate()

    def __str__(self):
        return self.title