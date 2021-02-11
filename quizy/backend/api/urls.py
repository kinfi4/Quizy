from django.urls import path
from api.views.quizzes_api import QuizCreateView, QuizListView, UserQuizzesView
from api.views.questions_api import QuestionsForQuizView
from api.views.variants_api import VariantsForQuestionView


urlpatterns = [
    path('quizzes', QuizListView.as_view()),
    path('quizzes/user/<int:pk>', UserQuizzesView.as_view()),
    path('questions/quiz/<int:pk>', QuestionsForQuizView.as_view()),
    path('variants/question/<int:pk>', VariantsForQuestionView.as_view()),
]
