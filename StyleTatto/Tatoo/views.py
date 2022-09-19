from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *


class CitasViewsets(viewsets.ModelViewSet):
    queryset = Citas.objects.all()
    serializer_class = CitasSerializer

class PortafolioTatuadoresViewsets(viewsets.ModelViewSet):
    queryset=Portafolio_Tatuadores.objects.all()
    serializer_class=PortafolioTatuadoresSerializers


class RegistroUsuarioViewsets(viewsets.ModelViewSet):
    queryset=RegistroUsuarios.objects.all()
    serializer_class=RegistroUsuariosSerializers

class RegistroTatuadoresViewsets(viewsets.ModelViewSet):
    queryset=RegistroTatuadores.objects.all()
    serializer_class=RegistroTatuadoresSerializers
