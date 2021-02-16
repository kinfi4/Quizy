from django.core.exceptions import ObjectDoesNotExist
from api.models import Quiz
from api.utils.random_code_generator import generate_random_code


def quiz_code_exists(quiz_code):
    try:
        ob = Quiz.objects.get(code=quiz_code)
        return ob is not None
    except:
        return False


def generate_unique_code():
    code = generate_random_code()
    while quiz_code_exists(quiz_code=code):
        code = generate_random_code()

    return code

