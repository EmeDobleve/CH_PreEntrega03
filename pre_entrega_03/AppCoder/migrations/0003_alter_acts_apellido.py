# Generated by Django 4.1.7 on 2023-04-15 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0002_remove_acts_descripcion_remove_acts_imagen_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acts',
            name='apellido',
            field=models.CharField(max_length=100),
        ),
    ]
