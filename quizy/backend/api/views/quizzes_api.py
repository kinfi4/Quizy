from rest_framework import generics
from django.http.request import HttpRequest

from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from api.serializers.serializers import QuizGetSerializer, QuizCreateSerializer, QuizUpdateSerializer

from api.models import Quiz


class QuizListView(generics.ListAPIView):
    serializer_class = QuizGetSerializer

    def get_queryset(self):
        return Quiz.objects.filter(is_private=False)


class UserQuizzesView(generics.ListAPIView):
    serializer_class = QuizGetSerializer

    def get_queryset(self):
        username = self.request.parser_context['kwargs'].get('username')
        return Quiz.objects.select_related('creator').filter(creator__username=username)


class QuizzesByTag(generics.ListAPIView):
    serializer_class = QuizGetSerializer

    def get_queryset(self):
        tag_names = self.request.query_params.get('tn')
        tag_names = ['#' + tn for tn in tag_names.split('%')]
        return Quiz.objects.filter(tags__tag_body__in=tag_names)


class QuizByIdView(generics.RetrieveAPIView):
    serializer_class = QuizGetSerializer

    def get_object(self):
        quiz_id = int(self.request.parser_context['kwargs'].get('pk'))
        return get_object_or_404(Quiz, id=quiz_id)


class UpdateQuizView(generics.UpdateAPIView):
    serializer_class = QuizUpdateSerializer

    def get_queryset(self):
        return Quiz.objects.all()


class CreateQuizView(APIView):
    def post(self, request: HttpRequest):
        quiz = QuizCreateSerializer(data=request.data)

        if quiz.is_valid(raise_exception=True):
            print(quiz.save())

        return Response(status=201)
