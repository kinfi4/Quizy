from django.urls import path
from api.views.quizzes_api import QuizCreateView, QuizListView, UserQuizzesView
from api.views.questions_api import QuestionsForQuizView
from api.views.variants_api import VariantsForQuestionView
from api.views.users_api import UsersView
from api.views.tags_api import TagsView


urlpatterns = [
    path('quizzes', QuizListView.as_view()),
    path('quizzes/user/<int:pk>', UserQuizzesView.as_view()),
    path('questions/quiz/<int:pk>', QuestionsForQuizView.as_view()),
    path('variants/question/<int:pk>', VariantsForQuestionView.as_view()),
    path('users', UsersView.as_view()),
    path('tags', TagsView.as_view()),
]
