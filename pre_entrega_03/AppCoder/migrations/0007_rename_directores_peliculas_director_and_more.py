# Generated by Django 4.1.7 on 2023-04-15 22:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0006_alter_peliculas_directores'),
    ]

    operations = [
        migrations.RenameField(
            model_name='peliculas',
            old_name='directores',
            new_name='director',
        ),
        migrations.RemoveField(
            model_name='peliculas',
            name='act_destacados',
        ),
        migrations.RemoveField(
            model_name='peliculas',
            name='generos',
        ),
        migrations.RemoveField(
            model_name='peliculas',
            name='tags',
        ),
        migrations.AddField(
            model_name='peliculas',
            name='act_destacado',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='AppCoder.acts'),
        ),
        migrations.AddField(
            model_name='peliculas',
            name='genero',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='AppCoder.generos'),
        ),
        migrations.AddField(
            model_name='peliculas',
            name='tag',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='AppCoder.tags'),
        ),
    ]