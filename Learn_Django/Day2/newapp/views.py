from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def verifyName(request):
    name = input("What is your name: ")
    return HttpResponse(name)

def home(request):
    return render(request,'index.html')

def form(request):
    return render(request,'test.html')