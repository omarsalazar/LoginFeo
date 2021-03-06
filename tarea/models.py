from django.db import models
from materia.models import datosmateria
from django.contrib.auth.models import User


class tarea(models.Model):
    id_tarea = models.CharField(blank=False, null=False, max_length=100)
    descripcion = models.CharField(blank=False, null=False, max_length=100)
    materia = models.ForeignKey(datosmateria, blank=False, null=False)
    fecha_entrega = models.DateField(blank=False, null=False)
    user = models.ForeignKey(User, blank=True, null=True)


class alarmatarea(models.Model):
    id_alarmatarea = models.CharField(blank=True, null=True, max_length=100)
    fecha_entrega = models.DateField(blank=True, null=True)
    id_tarea = models.ForeignKey(tarea, blank=False, null=False)


class repeticiontarea(models.Model):
    horaalarma = models.TimeField(blank=True, null=True)
    id_alarmatarea = models.ForeignKey(alarmatarea, blank=False, null=False)
