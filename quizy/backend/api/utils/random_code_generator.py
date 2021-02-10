from string import printable
from random import choice


def generate_random_code(length=8):
    return ''.join([choice(printable[:62]) for _ in range(length)])
