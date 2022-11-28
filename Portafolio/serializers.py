#Libraries
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import ValidationError
from rest_framework import status
from . import models


class PostPortafolio(serializers.ModelSerializer):
    class Meta:
        model = models.portafolio
        fields = '__all__' 