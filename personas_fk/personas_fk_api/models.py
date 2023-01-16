from django.db import models
from django.db.models.fields import uuid

# Create your models here.


class Genero(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    descripcion = models.CharField(max_length=50, blank=False, null=False)


class TipoEstudiante(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    descripcion = models.CharField(max_length=50, blank=False, null=False)


class Persona(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    identificacion = models.CharField(max_length=50, blank=False, null=False)
    nombre = models.CharField(max_length=50, blank=False, null=False)
    apellido = models.CharField(max_length=50, blank=False, null=False)
    edad = models.PositiveIntegerField(blank=False, null=False)
    tipoEstudiante = models.ForeignKey(
        "TipoEstudiante",
        on_delete=models.PROTECT,
        related_name="type_student",
        null=False,
    )
    genero = models.ForeignKey(
        "Genero",
        on_delete=models.PROTECT,
        related_name="gender",
        null=False,
    )
