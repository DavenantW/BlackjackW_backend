from django.db import models


class Users(models.Model):
    name = models.CharField(max_length=32)
    email = models.CharField(max_length=256, unique=True)
    password_hash = models.CharField(max_length=128)


class Statistics(models.Model):
    games = models.IntegerField()
    wins = models.IntegerField()
    money = models.IntegerField()
