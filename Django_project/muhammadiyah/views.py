from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
# Create your views here.
def index(request):
    return render(request, 'index.html')

def App(request):
    return render(request, 'App.html')

def about(request):
    return render(request, 'about.html')