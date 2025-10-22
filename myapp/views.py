from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse
import pyttsx3

robot = pyttsx3.init()


# views here.

def mainmenu(request):
    return render(request, 'myapp/mainmenu.html')

def index(request):
    return render(request, 'myapp/welcome-page.html')

def game(request):
    return render(request, 'myapp/game.html')

@csrf_exempt
def ai_speech(request):
    if request.method == "POST":
        text = request.POST.get("text", "")
        if text:
                ai_says(text)
                return HttpResponse("OK", status=200)
        return HttpResponse("Error: no text provided", status=400)
    return HttpResponse("Error: invalid method", status=405)


# util functions here


def ai_says(command):
    robot.say(command)
    robot.runAndWait()
