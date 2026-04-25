from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('apply/<int:pk>/', views.apply, name='apply'),
]