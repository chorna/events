from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# Create your models here.


class Room(models.Model):
    name = models.CharField(max_length=50)
    capacity = models.IntegerField(unique=True)

    def __str__(self) -> str:
        return self.name


class Event(models.Model):
    PUBLIC_CHOICE = 1
    PRIVATE_CHOICE = 2
    TYPE_CHOICES = (
        (PUBLIC_CHOICE, 'Public'),
        (PRIVATE_CHOICE, 'Private'),
    )
    room = models.OneToOneField("Room", on_delete=models.CASCADE)
    type = models.IntegerField(choices=TYPE_CHOICES)
    name = models.CharField(max_length=50)
    capacity = models.IntegerField()
    date = models.DateField(
        auto_now=False,
        auto_now_add=False,
        unique=True
    )

    def __str__(self) -> str:
        return self.name


class Books(models.Model):
    client = models.ForeignKey(
        User,
        related_name="books",
        on_delete=models.CASCADE
        )
    event = models.ForeignKey(
        "Event",
        related_name="books",
        on_delete=models.CASCADE
        )
    is_active = models.BooleanField(default=True)


