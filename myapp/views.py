from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def mainmenu(request):
    return render(request, 'myapp/mainmenu.html')

def index(request):
    return render(request, 'myapp/welcome-page.html')

def game(request):
    return render(request, 'myapp/game.html')
