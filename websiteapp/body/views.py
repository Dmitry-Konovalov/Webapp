from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    #print(request)
    return HttpResponse("hello word ")

def test(request):
    #print(request)
    return HttpResponse("<h1>Тестовая страница</h1>")
