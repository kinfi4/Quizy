from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class Tag(models.Model):
    tag_body = models.CharField(max_length=128, primary_key=True, unique=True, db_index=True)


class AnswerVariant(models.Model):
    id = models.IntegerField(primary_key=True)
    answer_body = models.CharField(max_length=248)
    is_correct = models.BooleanField(default=False)


class Question(models.Model):
    id = models.IntegerField(primary_key=True)
    question = models.CharField(max_length=1024)
    variants = models.ForeignKey(AnswerVariant, on_delete=models.CASCADE)


class Quiz(models.Model):
    id = models.IntegerField(primary_key=True)
    is_private = models.BooleanField(default=False)
    code = models.CharField(max_length=8, db_index=True)

    title = models.CharField(max_length=128, null=False)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True, null=True)
    questions = models.ForeignKey(Question, on_delete=models.CASCADE, null=False)
    tags = models.ManyToManyField(Tag, db_index=True)
