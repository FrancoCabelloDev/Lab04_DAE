from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.management_dashboard, name='management_dashboard'),
]
