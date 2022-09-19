from datetime import datetime
from tkinter import CASCADE
from django.db import models

class Departamentos (models.Model):
    nombre = models.CharField(max_length=50)

class Localidades(models.Model):
    fk_departamento = models.ForeignKey(Departamentos, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=30)
class RegistroUsuarios (models.Model):
    id_user = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.TextField()
    email = models.TextField(max_length=90)
    fecha_nacimiento = models.DateField()
    contraseña = models.TextField(max_length=20)
    estado = models.CharField(default='A', max_length=1)

class RegistroTatuadores (models.Model):
    id_tatuador = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.TextField()
    genero = models.TextField()
    fecha_nacimiento = models.DateField()
    ciudad = models.ForeignKey(Localidades, on_delete=models.CASCADE)
    departamento = models.ForeignKey(Departamentos, on_delete=models.CASCADE)
    direccion = models.TextField()
    email = models.TextField(max_length=90)
    experiencia = models.CharField(max_length=3)
    descripcion=models.TextField(max_length=150,blank=True,default='')
    contraseña = models.TextField(max_length=20)
    estado = models.CharField(default='A', max_length=1)

class Citas(models.Model):
    id_cita = models.BigAutoField(primary_key=True)
    Tatuador = models.ForeignKey(RegistroTatuadores, on_delete=models.CASCADE)
    usuario = models.ForeignKey(RegistroUsuarios, on_delete=models.CASCADE)
    Fecha = models.DateField()
    Hora = models.TimeField()
    Imagen = models.ImageField()
    Descripcion = models.CharField(max_length=150, blank=False, default='')


class Portafolio_Tatuadores(models.Model):
    id_publicacion = models.BigAutoField(primary_key=True)
    fecha_publicacion=models.DateTimeField(default=datetime.now())
    tatuador=models.ForeignKey(RegistroTatuadores, on_delete=models.CASCADE)
    imagen=models.ImageField()
    descripcion=models.TextField(max_length=150,blank=True,default='')

class likes(models.Model):
    id_likes = models.BigAutoField(primary_key=True)
    fk_tatuador = models.ForeignKey(RegistroTatuadores, on_delete=models.CASCADE)
    likes = models.IntegerField()

