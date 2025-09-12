from django.urls import path
from .views import  CreateInflowView, InflowDeleteView, pay_inflow
from . import views

urlpatterns = [
    path('inflows/', CreateInflowView.as_view(), name='inflow_list'),
    #path('outflows/delete/<int:pk>/', views.OutflowDeleteView.as_view(), name='outflow_delete'),
    path('inflows/<int:pk>/detail/', views.OutflowDetailView.as_view(), name='inflow_detail'),
    path('inflows/update/<int:pk>/', views.OutflowUpdateView.as_view(), name='inflow_update'),
    path('inflows/pay/<int:pk>/', views.pay_inflow, name='inflow_pay'),
    path('inflows/report/', views.inflow_report, name='inflow_report'),
]
