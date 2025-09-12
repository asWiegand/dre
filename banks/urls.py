# banks/urls.py
from django.urls import path
from .views import BankCreate, BankDeleteView, BankUpdateView

urlpatterns = [
    path('bank_list/', BankCreate.as_view(), name='bank_list'),
    path('banks/delete/<int:pk>/', BankDeleteView.as_view(), name='bank_delete'),
    path('banks/update/<int:pk>/', BankUpdateView.as_view(), name='bank_update'),
]
