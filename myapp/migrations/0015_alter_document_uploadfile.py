# Generated by Django 4.1.2 on 2023-01-13 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_alter_docentes_id_docente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='uploadfile',
            field=models.FileField(upload_to='files/'),
        ),
    ]
