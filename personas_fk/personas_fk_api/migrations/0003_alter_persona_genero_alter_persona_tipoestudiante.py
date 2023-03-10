# Generated by Django 4.1.5 on 2023-01-10 05:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("personas_fk_api", "0002_persona_edad"),
    ]

    operations = [
        migrations.AlterField(
            model_name="persona",
            name="genero",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="gender",
                to="personas_fk_api.genero",
            ),
        ),
        migrations.AlterField(
            model_name="persona",
            name="tipoEstudiante",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="type_student",
                to="personas_fk_api.tipoestudiante",
            ),
        ),
    ]
