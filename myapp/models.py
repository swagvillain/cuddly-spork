from django.db import models

# Create your models here.

class Player(models.Model):
    player_name = models.CharField(max_length=30)

class ScoreLog(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True) # when player got score
    score = models.IntegerField(default=0)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-score']  # highest score first
