from django.contrib import admin
from .models import Quiz, Question, User, AnswerVariant, Tag

admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(AnswerVariant)
admin.site.register(Tag)
