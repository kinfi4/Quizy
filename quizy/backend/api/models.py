from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class Tag(models.Model):
    tag_body = models.CharField(max_length=128, primary_key=True, unique=True, db_index=True)


class Quiz(models.Model):
    is_private = models.BooleanField(default=False)
    code = models.CharField(max_length=8, db_index=True)

    title = models.CharField(max_length=128, null=False)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True, null=True)
    tags = models.ManyToManyField(Tag, db_index=True, blank=True)


class Question(models.Model):
    question = models.CharField(max_length=1024)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)


class AnswerVariant(models.Model):
    body = models.CharField(max_length=248)
    is_correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
