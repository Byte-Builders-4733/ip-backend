from django.db import models

class Word(models.Model):
    name = models.SlugField('Слово')
    text = models.TextField("Значение слова")

    group = models.ForeignKey(
        'Group',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='posts'
    )
    complexity = models.SlugField()
