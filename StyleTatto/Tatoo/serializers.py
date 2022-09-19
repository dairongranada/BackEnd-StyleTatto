from rest_framework import serializers
from .models import *

class CitasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Citas
        fields= "__all__"

class PortafolioTatuadoresSerializers(serializers.ModelSerializer):
    class Meta:
        model= Portafolio_Tatuadores
        fields= "__all__"
       


# FORMULARIOS  REGISTROS

class RegistroUsuariosSerializers(serializers.ModelSerializer):
    class Meta:
        model= RegistroUsuarios
        fields= "__all__"

class RegistroTatuadoresSerializers(serializers.ModelSerializer):
    class Meta:
        model= RegistroTatuadores
        fields= "__all__"