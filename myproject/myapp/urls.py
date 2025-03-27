from django.urls import path
from .views import home  # Ensure you have a home view in your views.py

urlpatterns = [
    path('', home, name='home'),
]
