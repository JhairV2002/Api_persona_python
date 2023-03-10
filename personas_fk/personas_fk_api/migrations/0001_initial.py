# Generated by Django 4.1.5 on 2023-01-10 02:24

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Genero",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("descripcion", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="TipoEstudiante",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("descripcion", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Persona",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("identificacion", models.CharField(max_length=50)),
                ("nombre", models.CharField(max_length=50)),
                ("apellido", models.CharField(max_length=50)),
                (
                    "genero",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="gender",
                        to="personas_fk_api.genero",
                    ),
                ),
                (
                    "tipoEstudiante",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="type_student",
                        to="personas_fk_api.tipoestudiante",
                    ),
                ),
            ],
        ),
    ]
