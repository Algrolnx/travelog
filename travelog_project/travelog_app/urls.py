from .import views
from django.urls import path

urlpatterns = [
    path('', views.trip_list, name='trip_list'),
    path('<int:pk>/', views.trip_detail, name='trip_detail'),
]
