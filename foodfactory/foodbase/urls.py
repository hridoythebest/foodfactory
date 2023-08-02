from django.urls import path
from . import views

urlpatterns = [
    path('', views.foodbase, name = 'foodbase'),
    
]