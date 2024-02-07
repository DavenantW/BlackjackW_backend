from django.db import models

class User(models.Model):
    name = models.CharField('name')
    email = models.EmailField('email')
    password = models.CharField('password')
    def __str__(self):
        return f'{self.name}({self.pk})'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'