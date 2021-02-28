from django.urls import path, re_path
from frontend.views import index, welcome, app

urlpatterns = [
    path('', index),
    path('welcome', welcome),
    re_path(r'^app/.*', app),
]
