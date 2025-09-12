from django.urls import path
from .views import  CreatePaymentView

urlpatterns = [
    path('payments/', CreatePaymentView.as_view(), name='payment_list'),
]
