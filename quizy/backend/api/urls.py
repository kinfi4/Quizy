from django.urls import path
from .views import Quizzes


urlpatterns = [
    path('quizzes', Quizzes.as_view())
]
