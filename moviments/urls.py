from django.urls import path
from .views import  MovimentDeleteView, MovimentDetailView, MovimentUpdateView, MovimentListView, MovimentCreateView

urlpatterns = [
    path('moviments/create/', MovimentCreateView.as_view(), name='moviment_create'),
    path('moviments/delete/<int:pk>/', MovimentDeleteView.as_view(), name='moviment_delete'),
    path('moviments/update/<int:pk>/', MovimentUpdateView.as_view(), name='moviment_update'),
    path('moviments/detail/<int:pk>/', MovimentDetailView.as_view(), name='moviment_detail'),
    path('moviments/', MovimentListView.as_view(), name='moviment_list'),
]
