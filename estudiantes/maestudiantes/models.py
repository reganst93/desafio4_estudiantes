from django.db import models

# Create your models here.
class Direccion(models.Model):
    id = models.AutoField(primary_key=True)
    calle = models.CharField(max_length=50, null=False, blank=False)
    numero = models.CharField(max_length=10, null=False, blank=False)
    dpto = models.CharField(max_length=10, blank=True)
    comuna = models.CharField(max_length=50, null=False, blank=False)
    ciudad = models.CharField(max_length=50, null=False, blank=False)
    region = models.CharField(max_length=50, null=False, blank=False)
    estudiante = models.ForeignKey('Estudiante', on_delete=models.CASCADE)


class Estudiante(models.Model):
    id = models.AutoField(primary_key=True)
    rut = models.CharField(max_length=9, unique=True, null=False, blank=False)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    apellido = models.CharField(max_length=50, null=False, blank=False)
    fecha_nac = models.DateField(null=False, blank=False)
    activo = models.BooleanField(default=False)
    creacion_registro = models.DateField(auto_now_add=True, null=False, blank=False)
    modificacion_registro = models.DateField(auto_now=True)
    creado_por = models.CharField(max_length=50, null=True, blank=True)

class Curso(models.Model):
    codigo = models.CharField(max_length=9, unique=True, null=False, blank=False)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    version = models.IntegerField(null=True)
    profesor = models.ForeignKey('Profesor', on_delete=models.SET_NULL, null=True)
    estudiantes = models.ManyToManyField(Estudiante, related_name='cursos')


class Profesor(models.Model):
    rut = models.CharField(max_length=9, unique=True, null=False, blank=False)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    apellido = models.CharField(max_length=50, null=False, blank=False)
    activo = models.BooleanField(default=False)
    creacion_registro = models.DateField(auto_now_add=True, null=False, blank=False)
    modificacion_registro = models.DateField(auto_now=True)
    creado_por = models.CharField(max_length=50, null=True, blank=True)