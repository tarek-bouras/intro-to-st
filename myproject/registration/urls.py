# registration/urls.py
from django.urls import path
from .views import register

urlpatterns = [
    path('', register, name='register'),
]
