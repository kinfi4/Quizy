from api.models import Quiz


def quiz_code_exists(quiz_code):
    return Quiz.objects.get(code=quiz_code) is None
