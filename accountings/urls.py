from django.urls import path
from .views import AccountingListView, AccountingCreateView, AccountingUpdateView, AccountingDeleteView

urlpatterns = [
    path('accountings/', AccountingListView.as_view(), name='accounting_list'),
    path('accountings/create/', AccountingCreateView.as_view(), name='accounting_create'),
    path('accountings/update/<int:pk>/', AccountingUpdateView.as_view(), name='accounting_update'),
    path('accountings/delete/<int:pk>/', AccountingDeleteView.as_view(), name='accounting_delete'),
]
