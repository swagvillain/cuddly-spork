from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Player, ScoreLog
import pyttsx3
import json

robot = pyttsx3.init()
robot.setProperty('rate', 150)


# views here.

def mainmenu(request):
    return render(request, 'myapp/mainmenu.html')

def highscores(request):
    scores = ScoreLog.objects.all()[:10]
    
    # add a lil logic here
    last_score = None
    last_rank = 0

    for idx, item in enumerate(scores, start=1):
        if item.score == last_score:
            item.rank = last_rank
        else: 
            item.rank = idx
            last_rank = idx

        last_score = item.score

    return render(request, 'myapp/highscores.html', {'scores': scores})

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


def log_player_score(request):
    try:
        payload = json.loads(request.body)
    except:
        return JsonResponse({"error": "invalid json"}, status=400)

    name = payload.get("player")
    score = payload.get("score")

    if not name or score is None:
        return JsonResponse({"error": "missing fields"}, status=400)

    player, _ = Player.objects.get_or_create(player_name=name)

    ScoreLog.objects.create(player=player, score=score)

    return JsonResponse({"status": "ok"})
