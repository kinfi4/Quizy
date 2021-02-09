from django.urls import path
from backend.api.views import main

urlpatterns = [
    path('', main)
]
