# Generated by Django 4.1.2 on 2023-01-30 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0021_asistencia_in_codigo_curso_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AsignaTarea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(default='defauld value', max_length=40)),
                ('fechaIni', models.DateField()),
                ('fechaFin', models.DateField()),
            ],
        ),
    ]
