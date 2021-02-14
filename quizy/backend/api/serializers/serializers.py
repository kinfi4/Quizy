from rest_framework import serializers
from api.models import Question, Quiz, Tag, User, AnswerVariant


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['tag_body']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class VariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerVariant
        fields = ('body', 'is_correct')


class QuestionSerializer(serializers.ModelSerializer):
    variants = VariantSerializer(many=True)

    class Meta:
        model = Question
        fields = ('variants', 'question')


class QuizSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)
    tags = TagSerializer(many=True)
    creator = UserSerializer()

    class Meta:
        model = Quiz
        fields = '__all__'
