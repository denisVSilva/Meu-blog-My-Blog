from django.shortcuts import render
from django.http import HttpResponse

def Homepage(request):
    return render(request, "blog/Homepage.html")

def Pythonpage(request):
    return HttpResponse("in progress")


def blenderpage(request):
    return HttpResponse("in progress")