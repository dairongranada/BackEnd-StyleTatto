from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model


# Create your models here.

Users = get_user_model()


class Quotes(models.Model):
    id_quotes = models.BigAutoField(primary_key=True)
    date = models.DateField()
    time = models.TimeField()
    img = models.CharField(max_length=150)
    description = models.CharField(max_length=150, blank=False)
    userID = models.ForeignKey(Users, on_delete=models.CASCADE, related_name="perfilUser")
    userName = models.CharField(max_length=150)
    artist_tattoo = models.ForeignKey(Users, on_delete=models.CASCADE, related_name= "perfilTattoo")
    userTatto = models.CharField(max_length=150)

    isActive = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.id_quotes