from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def verifyName(request):
    name = input("What is your name: ")
    return HttpResponse(name)

def home(request):
    name = "Uyghur"
    age = 20
    return render(request,'index.html',{'name':name,'age':age})

def form(request):
    return render(request,'test.html')