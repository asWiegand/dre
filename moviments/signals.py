from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Moviment
from decimal import Decimal


@receiver(post_save, sender=Moviment)
def update_bank_balance_on_save(sender, instance, created, **kwargs):
    value = instance.value
    bank = instance.bank_id
    acc_type = instance.accounting.type

    # Se for uma nova movimentação
    if created:
        if acc_type == 'E':
            bank.balance += value
        else:  # Saída
            bank.balance -= value
        bank.save()
    else:
        # Atualização: precisa verificar o valor anterior
        old_instance = sender.objects.get(pk=instance.pk)
        diff = instance.value - old_instance.value

        # Corrigir saldo removendo valor antigo e aplicando novo
        if old_instance.accounting.type == 'E':
            bank.balance -= old_instance.value
        else:
            bank.balance += old_instance.value

        if acc_type == 'E':
            bank.balance += instance.value
        else:
            bank.balance -= instance.value

        bank.save()


@receiver(post_delete, sender=Moviment)
def update_bank_balance_on_delete(sender, instance, **kwargs):
    value = instance.value
    bank = instance.bank_id
    acc_type = instance.accounting.type

    if acc_type == 'E':
        bank.balance -= value
    else:
        bank.balance += value
    bank.save()
