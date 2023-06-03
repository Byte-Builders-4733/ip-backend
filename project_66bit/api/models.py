from django.db import models

class Word(models.Model):
    term = models.CharField(max_length=20)
    definition = models.TextField(max_length=200)
    category = models.CharField(max_length=20)
    complexity = models.IntegerField()