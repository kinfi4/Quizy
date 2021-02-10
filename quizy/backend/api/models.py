from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Quiz(models.Model):
    id = models.IntegerField(primary_key=True)
    question = models.CharField(max_length=1024)
    variants = models.CharField(max_length=2048)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
