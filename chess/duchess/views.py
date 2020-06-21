from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def play(request):
    return HttpResponse("Play")

def login(request):
    return render(request,'accounts/login.html')

def register(request):
    return HttpResponse("register")

def home(request):
    return render(request,'play/home.html')