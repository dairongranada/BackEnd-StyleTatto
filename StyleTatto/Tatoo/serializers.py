from dataclasses import field
from pyexpat import model
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
        fields= (
            'fecha_nacimiento',
            'nombre',
            'apellido',
            'telefono',
            'genero',
            'contraseña'
        )

class RegistroTatuadoresSerializers(serializers.ModelSerializer):
    class Meta:
        model= RegistroTatuadores
        fields= (
            'fecha_nacimiento',
            'nombre',
            'apellido',
            'telefono',
            'genero',
            'contraseña',
            'departamento',
            'ciudad',
            'direccion',
            'email',
            'descripcion',
            'experiencia'
        )

class RegistroDepartamentoserializers(serializers.ModelSerializer):

    class Meta:
        model = Departamentos
        fields= "__all__"

class RegistroLocalidadeserializers(serializers.ModelSerializer):

    class Meta:
        model = Localidades
        fields = "__all__"