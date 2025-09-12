from django.urls import path
from .views import AccountingCreateView, AccountingDeleteView
#, MovimentDetailView, MovimentUpdateView

urlpatterns = [
    path('accounting_list/', AccountingCreateView.as_view(), name='accounting_list'),
    path('accountings/delete/<int:pk>/', AccountingDeleteView.as_view(), name='accounting_delete'),
    #path('moviments/update/<int:pk>/', MovimentUpdateView.as_view(), name='moviment_update'),
    #path('moviments/detail/<int:pk>/', MovimentDetailView.as_view(), name='moviment_detail'),
]
