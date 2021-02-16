from rest_framework import serializers
from api.models import Question, Quiz, Tag, User, AnswerVariant
from api.database.generate_unique_code import generate_unique_code


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
    questions = QuestionSerializer(many=True, read_only=True)
    tags = TagSerializer(many=True, read_only=True, required=False)
    creator = UserSerializer()

    class Meta:
        model = Quiz
        fields = '__all__'


class QuizCreateSerializer(serializers.Serializer):
    is_private = serializers.BooleanField(default=False)
    title = serializers.CharField(max_length=128, required=True)
    creator_username = serializers.CharField(max_length=512)
    tags = serializers.ListField()
    questions = QuestionSerializer(many=True, required=True)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data: dict):
        validated_data.update({
            'code': generate_unique_code(),
            'creator': User.objects.filter(username=validated_data.pop('creator_username')).first()
        })

        tags = self.create_tags_from_tag_data(validated_data.pop('tags'))
        questions_data = validated_data.pop('questions')

        quiz = Quiz.objects.create(**validated_data)
        quiz.save()

        questions = self.create_questions_from_questions_data(questions_data, quiz)

        quiz.tags.set(tags)
        quiz.questions.set(questions)
        quiz.save()

        return quiz

    @staticmethod
    def create_tags_from_tag_data(tags_data):
        tags = []
        for tag in tags_data:
            tag = tag[1:] if tag.startswith('#') else tag
            tag_object = Tag(tag_body=tag)
            tag_object.save()
            tags.append(tag_object)

        return tags

    @staticmethod
    def create_questions_from_questions_data(questions_data, quiz):
        questions = []
        for question_data in questions_data:
            question = Question(question=question_data['question'], quiz=quiz)
            question.save()

            variants = [AnswerVariant(body=variant['body'], is_correct=variant['is_correct'], question=question) for
                        variant in question_data['variants']]

            question.variants.set(variants, bulk=False)
            questions.append(question)

        return questions

# {
#         "questions": [
#             {
#                 "variants": [
#                     {
#                         "body": "12",
#                         "is_correct": true
#                     },
#                     {
#                         "body": "123",
#                         "is_correct": false
#                     }
#                 ],
#                 "question": "How old are u?"
#             }
#         ],
#         "tags": ["myquiz"],
#         "creator_username": "kinfi4",
#         "is_private": false,
#         "title": "Trying to fix it"
#     }
