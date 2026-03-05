from django.urls import path
from .views import SupplierListView, SupplierCreateView, SupplierUpdateView, SupplierDeleteView

urlpatterns = [
    path('suppliers/', SupplierListView.as_view(), name='supplier_list'),
    path('suppliers/create/', SupplierCreateView.as_view(), name='supplier_create'),
    path('suppliers/update/<int:pk>/', SupplierUpdateView.as_view(), name='supplier_update'),
    path('suppliers/delete/<int:pk>/', SupplierDeleteView.as_view(), name='supplier_delete'),
]
