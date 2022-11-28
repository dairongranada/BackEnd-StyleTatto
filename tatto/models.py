from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class Tattoo_artist (models.Model):
    img = models.TextField(max_length=150)
    create = models.DateTimeField(auto_now_add=True)
    departament = models.TextField(max_length=150)
    municipio = models.TextField(max_length=150)
    direction = models.TextField(max_length=150)
    experience = models.IntegerField()
    description=models.TextField(max_length=150)
    artist = models.ForeignKey(User, on_delete=models.CASCADE, related_name="PerfilProfesional")

    def __str__(self) -> str:
        return (self.id)
    

