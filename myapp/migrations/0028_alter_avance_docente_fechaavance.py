# Generated by Django 4.1.2 on 2023-02-05 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0027_remove_registro_alumnos_apellidos_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avance_docente',
            name='FechaAvance',
            field=models.DateTimeField(),
        ),
    ]
