from django.shortcuts import render
from rest_framework import generics
from .serializers import QuizSerializer


class Quizzes(generics.CreateAPIView):
    serializer_class = QuizSerializer




