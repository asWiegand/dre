from django.urls import path
from .views import OutflowListView, CreateOutflowView, OutflowDeleteView, OutflowDetailView, pay_outflow, OutflowUpdateView, outflow_report
from . import views

urlpatterns = [
    path('outflows/', OutflowListView.as_view(), name='outflow_list'),
    path('outflows/create/', CreateOutflowView.as_view(), name='outflow_create'),
    path('outflows/delete/<int:pk>/', OutflowDeleteView.as_view(), name='outflow_delete'),
    path('outflows/<int:pk>/detail/', OutflowDetailView.as_view(), name='outflow_detail'),
    path('outflows/update/<int:pk>/', OutflowUpdateView.as_view(), name='outflow_update'),
    path('outflows/pay/<int:pk>/', views.pay_outflow, name='outflow_pay'),

    path('outflows/report/', views.outflow_report, name='outflow_report'),
]
