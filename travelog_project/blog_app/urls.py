from .import views
from django.urls import path

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:pk>/', views.post_detail, name='post_detail'),
    path('create/', views.create_post, name='create_post'),
]
