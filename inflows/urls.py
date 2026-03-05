from django.urls import path
from .views import InflowListView, CreateInflowView, InflowDeleteView, pay_inflow, InflowDetailView, InflowUpdateView, inflow_report
from . import views

urlpatterns = [
    path('inflows/', InflowListView.as_view(), name='inflow_list'),
    path('inflows/create/', CreateInflowView.as_view(), name='inflow_create'),
    path('inflows/delete/<int:pk>/', InflowDeleteView.as_view(), name='inflow_delete'),
    path('inflows/<int:pk>/detail/', InflowDetailView.as_view(), name='inflow_detail'),
    path('inflows/update/<int:pk>/', InflowUpdateView.as_view(), name='inflow_update'),
    path('inflows/pay/<int:pk>/', views.pay_inflow, name='inflow_pay'),

    path('inflows/report/', views.inflow_report, name='inflow_report'),
]
