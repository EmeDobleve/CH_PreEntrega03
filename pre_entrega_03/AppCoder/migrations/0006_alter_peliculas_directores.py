# Generated by Django 4.1.7 on 2023-04-15 22:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0005_rename_director_peliculas_directores_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peliculas',
            name='directores',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='AppCoder.directores'),
        ),
    ]