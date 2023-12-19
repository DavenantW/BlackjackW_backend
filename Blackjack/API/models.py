from django.db import models


#Создал таблицу для теста sqllite3


class TestModel(models.Model):
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.title