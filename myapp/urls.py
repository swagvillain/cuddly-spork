from django.urls import path

from . import views

urlpatterns = [
        path("", views.index, name="index"),
        path('mainmenu', views.mainmenu, name='mainmenu'),
        path('game', views.game, name='game'),
        path('ai_speech/', views.ai_speech, name='ai_speech'),
        path('highscores', views.highscores, name='highscores'),
        path("log_player_score/", views.log_player_score, name="log_player_score"),
        ]
