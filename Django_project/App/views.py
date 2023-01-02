from django.shortcuts import render 

def index(request):
    return render(request, 'App.html')
# Create your views here.