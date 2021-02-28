from django.shortcuts import render


def index(request):
    return render(request, 'frontend/index.html')


def welcome(request):
    return render(request, 'frontend/index.html')


def app(request):
    return render(request, 'frontend/index.html')
