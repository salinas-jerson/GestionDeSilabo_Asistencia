# Generated by Django 4.1.2 on 2022-12-26 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_cargaacademica_id_docente_alter_cargaacademica_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cargaacademica',
            name='id_docente',
            field=models.PositiveIntegerField(),
        ),
    ]
