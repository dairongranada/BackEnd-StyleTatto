from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class disponibilidadModel (models.Model):
    dispo = models.BooleanField()
    like = models.IntegerField()
    iDispo = models.ForeignKey(User, on_delete=models.CASCADE, related_name="iDispo")


    def __str__(self) -> str:
        return (self.id)
    

