# banks/urls.py
from django.urls import path
from .views import BankListView, BankCreateView, BankDeleteView, BankUpdateView

urlpatterns = [
    path('banks/', BankListView.as_view(), name='bank_list'),
    path('banks/create/', BankCreateView.as_view(), name='bank_create'),
    path('banks/delete/<int:pk>/', BankDeleteView.as_view(), name='bank_delete'),
    path('banks/update/<int:pk>/', BankUpdateView.as_view(), name='bank_update'),
]
