from django.http import HttpResponse
from django import http
from django.shortcuts import render

# Create your views here.
def home(request):
    dict = {'template_var': 'this is var'}
    return render(request, 'home/index.html', context = dict)


def about(request):
    return HttpResponse("What the about")


def gallery(request):
    return HttpResponse("What the gallery")
