from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    USER = 'user'
    MODERATOR = 'moderator'
    ADMIN = 'admin'
    ROLE_CHOICE = (
        (USER, 'User'),
        (MODERATOR, 'Moderator'),
        (ADMIN, 'Admin'),
    )
    username = models.CharField(
        max_length=150,
        unique=True,
        blank=False,
        null=False,
    )
    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICE,
        default='user',
        blank=True
    )
    email = models.EmailField(
        max_length=254,
        unique=True,
        blank=False,
        null=False
    )
    confirmation_code = models.CharField(
        max_length=255,
        null=True,
        blank=False,
    )

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.username

    @property
    def is_admin(self):
        return self.role == self.ADMIN or self.is_superuser

    @property
    def is_moderator(self):
        return self.role == self.MODERATOR

    @property
    def is_user(self):
        return self.role == self.USER

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
    complexity = models.ForeignKey(
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )
