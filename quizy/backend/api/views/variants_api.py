from rest_framework import generics
from api.serializers.variant_serializer import VariantSerializer
from api.models import AnswerVariant


class VariantsForQuestionView(generics.ListAPIView):
    serializer_class = VariantSerializer

    def get_queryset(self):
        question_id = self.request.parser_context['kwargs'].get('pk')
        return AnswerVariant.objects.filter(question__id=question_id)
