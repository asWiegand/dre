from django.shortcuts import render
from banks.models import Bank
from accountings.models import Accounting
from moviments.models import Moviment
from django.db.models import Sum, Q
import json, calendar
from django.db.models.functions import ExtractMonth, ExtractYear

def home_view(request):
    # Dados de saldo por banco
    banks = Bank.objects.all()
    bank_labels = [bank.bank_name for bank in banks]
    bank_values = [float(bank.balance) for bank in banks]

    # Dados de movimentações por plano de contas (soma de value em Moviment)
    accounting_data = Accounting.objects.annotate(total=Sum('moviments__value'))
    accounting_labels = [acc.acc_name for acc in accounting_data]
    accounting_values = [float(acc.total or 0) for acc in accounting_data]

    context = {
        'bank_chart_data': json.dumps({'labels': bank_labels, 'values': bank_values}),
        'accounting_chart_data': json.dumps({'labels': accounting_labels, 'values': accounting_values}),
    }
    return render(request, 'home.html', context)

def report_view(request):
    month = request.GET.get('month')
    year = request.GET.get('year')
    try:
        year = int(year)
    except (TypeError, ValueError):
        year = None

    accountings = Accounting.objects.all()

    # Filtro base de movimentações
    moviments = Moviment.objects.all()
    if year:
        moviments = moviments.annotate(year=ExtractYear('moviment_date')).filter(year=year)
    if month:
        moviments = moviments.annotate(month=ExtractMonth('moviment_date')).filter(month=month)

    # Soma total por plano de contas com filtro aplicado
    accounting_data = accountings.annotate(
        total=Sum('moviments__value', filter=Q(moviments__in=moviments))
    )
    month_choices = [
    ("1", "Janeiro"), ("2", "Fevereiro"), ("3", "Março"),
    ("4", "Abril"), ("5", "Maio"), ("6", "Junho"),
    ("7", "Julho"), ("8", "Agosto"), ("9", "Setembro"),
    ("10", "Outubro"), ("11", "Novembro"), ("12", "Dezembro"),
    ]
    years_choices = Moviment.objects.dates('moviment_date', 'year', order='DESC')
    context = {
        "accountings": accounting_data,
        "year": year,
        "month": month,
        "years_choices":list(years_choices),
        "month_choices": month_choices,
    }
    return render(request, 'report.html', context)