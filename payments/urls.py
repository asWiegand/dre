from django.urls import path
from .views import PaymentListView, CreatePaymentView, PaymentUpdateView, PaymentDeleteView

urlpatterns = [
    path('payments/', PaymentListView.as_view(), name='payment_list'),
    path('payments/create/', CreatePaymentView.as_view(), name='payment_create'),
    path('payments/update/<int:pk>/', PaymentUpdateView.as_view(), name='payment_update'),
    path('payments/delete/<int:pk>/', PaymentDeleteView.as_view(), name='payment_delete'),
]
