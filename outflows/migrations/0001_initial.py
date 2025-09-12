
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accountings', '0001_initial'),
        ('payments', '0002_alter_payment_options_payment_name'),
        ('suppliers', '0002_alter_supplier_fantasy_name_alter_supplier_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Outflow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField()),
                ('expire_date', models.DateField()),
                ('title', models.CharField(max_length=15)),
                ('status', models.CharField(choices=[('PG', 'Pago'), ('NP', 'Não Pago')], max_length=2)),
                ('value', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('payment_date', models.DateField(blank=True, null=True)),
                ('accounting', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='outflows', to='accountings.accounting')),
                ('payment_methor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='outflows', to='payments.payment')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='outflows', to='suppliers.supplier')),
            ],
        ),
    ]
