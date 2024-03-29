# Generated by Django 4.1.2 on 2023-01-30 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0022_asignatarea'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigoAlumno', models.CharField(default='defauld value', max_length=6)),
                ('Apellido_Nombre', models.CharField(default='defauld value', max_length=40)),
                ('CodigoCurso', models.CharField(default='default value', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Lista_Alumnos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_Docente', models.CharField(default='default value', max_length=5)),
                ('Lista', models.FileField(upload_to='uploads/')),
                ('cod_curso', models.CharField(default='default value', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Registro_Alumnos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(default='defauld value', max_length=6)),
                ('Nombres', models.CharField(default='defauld value', max_length=40)),
                ('Apellidos', models.CharField(default='defauld value', max_length=40)),
                ('codigoCurso', models.CharField(default='default value', max_length=10)),
                ('Fecha', models.DateField()),
                ('observacion', models.CharField(default='defauld value', max_length=10)),
            ],
        ),
    ]
