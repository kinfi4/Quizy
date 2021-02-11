from django.urls import path
from api.views.quizzes_api import QuizCreateView, QuizListView, UserQuizzes
from api.views.questions_api import QuestionsForQuiz


urlpatterns = [
    path('quizzes', QuizListView.as_view()),
    path('quizzes/user/<int:pk>', UserQuizzes.as_view()),
    path('questions/quiz/<int:pk>', QuestionsForQuiz.as_view())
]
