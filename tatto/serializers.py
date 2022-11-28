#Libraries
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import ValidationError
from rest_framework import status
from . import models


class PostArtist(serializers.ModelSerializer):
    class Meta:
        model = models.Tattoo_artist
        fields = '__all__' 