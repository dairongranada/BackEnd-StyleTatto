from unittest.util import _MAX_LENGTH
from django.db import models

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser




# Cambiar Contraseña
from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail  

# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)

        user = self.model(
            email = email,
            **extra_fields
        )
        user.set_password(password)
        user.save()

        return user 

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError("El super usuario debe tener (is_staff) siendo Verdadero")


        if extra_fields.get('is_superuser') is not True:
            raise ValueError("El super usuario debe tener (is_superuser) siendo Verdadero")
        return self.create_user(email=email, password=password,**extra_fields)


class Users(AbstractUser):
    username = models.CharField(max_length=20)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=90 ,unique=True)
    image = models.CharField(max_length=100)
    rol = models.CharField(max_length=20)
    is_active= models.BooleanField(default=True)


    objects = CustomUserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username","first_name","last_name","rol","image"]


    def __str__(self):
        return self.username


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    email_plaintext_message = "{}?token={}".format(reverse('password_reset:reset-password-request'), reset_password_token.key)

    send_mail(
        # title:
        "Password Reset for {title}".format(title="Some website title"),
        # message:
        email_plaintext_message,
        # from:
        "OficialStyleTattoo@gmail.com",
        # contarseña: StyleTattoo_1 por si algo
        # to:
        [reset_password_token.user.email]
    )



