from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class portafolio (models.Model):
    img1 = models.TextField(max_length=150)
    img2 = models.TextField(max_length=150)
    img3 = models.TextField(max_length=150)
    img4 = models.TextField(max_length=150)
    img5 = models.TextField(max_length=150)
    idTatuador = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Portafolio")


    def __str__(self) -> str:
        return (self.img1)
    

