from django.db import models

class Circle(models.Model):
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
