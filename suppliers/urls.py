# banks/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('suppliers_list/', views.SupplierCreate.as_view(), name='supplier_list'),
    path('suppliers/delete/<int:pk>/', views.SupplierDeleteView.as_view(), name='supplier_delete'),
    path('suppliers/update/<int:pk>/', views.SupplierUpdateView.as_view(), name='supplier_update'),
]
