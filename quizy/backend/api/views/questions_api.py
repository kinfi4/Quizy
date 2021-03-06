from rest_framework import generics
from api.serializers.serializers import QuestionSerializer
from api.models import Question


class QuizQuestionsView(generics.ListAPIView):
    serializer_class = QuestionSerializer

    def get_queryset(self):
        quiz_id = self.request.parser_context['kwargs'].get('pk')
        return Question.objects.filter(quiz__id=quiz_id)
