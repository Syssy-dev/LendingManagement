from django.urls import path
from .views import create_lending

urlpatterns = [
    path('create-lending/', create_lending, name='create_lending'),
]
