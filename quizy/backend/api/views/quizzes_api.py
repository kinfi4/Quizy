from rest_framework import generics
from django.http.request import HttpRequest

from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from api.serializers.serializers import QuizSerializer

from api.models import Quiz


class QuizListView(generics.ListAPIView):
    serializer_class = QuizSerializer

    def get_queryset(self):
        return Quiz.objects.filter(is_private=False)


class UserQuizzesView(generics.ListAPIView):
    serializer_class = QuizSerializer

    def get_queryset(self):
        user_id = self.request.parser_context['kwargs'].get('pk')
        return Quiz.objects.filter(creator__id=user_id)


class QuizzesByTag(generics.ListAPIView):
    serializer_class = QuizSerializer

    def get_queryset(self):
        tag_names = self.request.query_params.get('tn')
        tag_names = ['#' + tn for tn in tag_names.split('%')]
        return Quiz.objects.filter(tags__tag_body__in=tag_names)


class QuizByIdView(generics.RetrieveAPIView):
    serializer_class = QuizSerializer

    def get_object(self):
        quiz_id = int(self.request.parser_context['kwargs'].get('pk'))
        return get_object_or_404(Quiz, id=quiz_id)


class UpdateQuizView(generics.UpdateAPIView):
    serializer_class = QuizSerializer

    def get_queryset(self):
        return Quiz.objects.all()


class CreateQuizView(APIView):
    def post(self, request: HttpRequest):
        quiz = QuizSerializer(data=request.data)

        if quiz.is_valid():
            quiz.save()

        return Response(status=201)
