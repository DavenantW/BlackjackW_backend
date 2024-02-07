from django.db import models

from users.models.users import User


class Statistic(models.Model):
    player = models.ForeignKey(User, models.CASCADE)
    money = models.PositiveBigIntegerField('money')
    games = models.PositiveBigIntegerField('games')
    wins = models.PositiveBigIntegerField('wins')

    class Meta:
        verbose_name = 'Статистика'
        verbose_name_plural = 'Статистики'
