from datetime import date
from django.db import models
from uuid import uuid4
# Create your models here.
class Player(models.Model):
    player_id= models.UUIDField(primary_key=True, default=uuid4)
    username = models.TextField(default="")
    xp = models.IntegerField(default=0)
    gold = models.IntegerField(default=0)

    class Meta:
        db_table = "player"
