from rest_framework import serializers
from api.models import AnswerVariant


class VariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerVariant
        fields = '__all__'
