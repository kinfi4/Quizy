from django.urls import path
from api.views.quizzes_api import QuizListView, UserQuizzesView, QuizzesByTag, QuizByIdView, \
    UpdateQuizView, CreateQuizView
from api.views.questions_api import QuizQuestionsView
from api.views.variants_api import QuestionVariantsView
from api.views.users_api import UsersView
from api.views.tags_api import TagsView

urlpatterns = [
    path('quizzes', QuizListView.as_view()),
    path('quizzes/<int:pk>', QuizByIdView.as_view()),
    path('quizzes/<int:pk>/update', UpdateQuizView.as_view()),
    path('quizzes/user/<int:pk>', UserQuizzesView.as_view()),
    path('quizzes/tag/<str:tn>', QuizzesByTag.as_view()),
    path('quizzes/tag', QuizzesByTag.as_view()),
    path('questions/quiz/<int:pk>', QuizQuestionsView.as_view()),
    path('variants/question/<int:pk>', QuestionVariantsView.as_view()),
    path('users', UsersView.as_view()),
    path('tags', TagsView.as_view()),
]
