from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("Hello Prayas- Good evening, we are all happy")
