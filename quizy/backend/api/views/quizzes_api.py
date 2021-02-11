from rest_framework import generics
from api.serializers.quiz_serializer import QuizSerializer

from api.models import Quiz


class QuizCreateView(generics.CreateAPIView):
    serializer_class = QuizSerializer


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
