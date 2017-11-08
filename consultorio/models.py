from django.db import models
from django.contrib import admin
# Create your models here.


class Paciente(models.Model):
    nombre  = models.CharField(max_length=30)
    edad = models.IntegerField()

    def __str__(self):
        return self.nombre

class Doctor(models.Model):
    nombre  =   models.CharField(max_length=30)
    especialidad = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre


class Analisis(models.Model):
    nombre    = models.CharField(max_length=60)
    costo      = models.IntegerField()
    pacientes   = models.ManyToManyField(Paciente, through='Consulta')


    def __str__(self):
        return self.nombre

class Consulta (models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    analisis = models.ForeignKey(Analisis, on_delete=models.CASCADE)

class ConsultaInLine(admin.TabularInline):
    model = Consulta
#muestra un campo extra al momento de insertar, como indicación que se pueden ingresar N actores.
    extra = 1


class PacienteAdmin(admin.ModelAdmin):
    inlines = (ConsultaInLine,)

class AnalisisAdmin (admin.ModelAdmin):
    inlines = (ConsultaInLine,)
