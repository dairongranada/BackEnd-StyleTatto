from rest_framework import serializers
from rest_framework.validators import ValidationError
from quotes.models import Quotes
from django.contrib.auth.models import User
from rest_framework import status

from .models import Quotes





class RegisterQuotes(serializers.ModelSerializer):
    class Meta:
        model = Quotes
        fields = '__all__'



class UpdateQuotes(serializers.ModelSerializer):
    class Meta:
        model = Quotes
        fields = ['isActive',]