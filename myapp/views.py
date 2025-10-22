from django.shortcuts import render
from django.http import HttpResponse
import pyttsx3

robot = pyttsx3.init()

# util functions here

def ai_says(command):
    robot.say("cool it works. I am speaking.")
    robot.runAndWait()
    return


# Create your views here.

def mainmenu(request):
    return render(request, 'myapp/mainmenu.html')

def index(request):
    return render(request, 'myapp/welcome-page.html')

def game(request):
    return render(request, 'myapp/game.html')

def ai_speech(request):
    ai_says(request)
    return HttpResponse("ok")
