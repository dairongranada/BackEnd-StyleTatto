from datetime import datetime
from tkinter import CASCADE
from django.db import models
from .choices import generos

class Departamentos (models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Localidades(models.Model):
    fk_departamento = models.ForeignKey(Departamentos, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.nombre
class RegistroUsuarios (models.Model):
    id_user = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.TextField()
    email = models.TextField(max_length=90)
    fecha_nacimiento = models.DateField()
    contraseña = models.TextField(max_length=20)
    estado = models.CharField(default='A', max_length=1)

    def nombre_Usuario(self):
        return "{} {}".format(self.nombre,self.apellido)

    def __str__(self):
        return self.nombre_Usuario()

class RegistroTatuadores (models.Model):
    id_tatuador = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.TextField()
    fecha_nacimiento = models.DateField()
    departamento = models.ForeignKey(Departamentos, on_delete=models.CASCADE)
    ciudad = models.ForeignKey(Localidades, on_delete=models.CASCADE)
    direccion = models.TextField()
    email = models.TextField(max_length=90)
    experiencia = models.CharField(max_length=3)
    descripcion=models.TextField(max_length=150,blank=True,default='')
    contraseña = models.TextField(max_length=20)
    estado = models.CharField(default='A', max_length=1)

    def nombre_Tatuador(self):
        return "{} {}".format(self.nombre,self.apellido)

    def __str__(self):
        return self.nombre_Tatuador()

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

