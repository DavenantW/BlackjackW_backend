from django.db import models


class Users(models.Model):
    name = models.CharField(max_length=32)
    email = models.CharField(max_length=256, unique=True)
    password_hash = models.IntegerField()
    games = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
    money = models.IntegerField(default=0)
