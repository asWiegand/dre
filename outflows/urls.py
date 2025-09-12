from django.urls import path
from .views import  CreateOutflowView, OutflowDeleteView, OutflowDetailView, pay_outflow
from . import views

urlpatterns = [
    path('outflows/', CreateOutflowView.as_view(), name='outflow_list'),
    path('outflows/delete/<int:pk>/', views.OutflowDeleteView.as_view(), name='outflow_delete'),
    path('outflows/<int:pk>/detail/', views.OutflowDetailView.as_view(), name='outflow_detail'),
    path('outflows/update/<int:pk>/', views.OutflowUpdateView.as_view(), name='outflow_update'),
    path('outflows/pay/<int:pk>/', views.pay_outflow, name='outflow_pay'),
    path('outflows/report/', views.outflow_report, name='outflow_report'),
]
