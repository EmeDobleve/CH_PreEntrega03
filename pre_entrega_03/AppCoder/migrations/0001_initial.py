# Generated by Django 4.1.7 on 2023-04-14 20:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Acts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('descripcion', models.CharField(max_length=150)),
                ('imagen', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Directores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('descripcion', models.CharField(max_length=150)),
                ('imagen', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Generos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('descripcion', models.CharField(max_length=150)),
                ('imagen', models.ImageField(upload_to='uploads/imgs/cat/')),
            ],
        ),
        migrations.CreateModel(
            name='Peliculas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=120)),
                ('anio', models.IntegerField()),
                ('imagen', models.CharField(max_length=60)),
                ('resumen', models.CharField(max_length=250)),
                ('imdb_link', models.CharField(max_length=150)),
                ('motivo_recomendacion', models.CharField(max_length=250)),
                ('act_destacados', models.ManyToManyField(help_text='Género/s', to='AppCoder.acts')),
                ('director', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='AppCoder.directores')),
                ('generos', models.ManyToManyField(help_text='Géneros de Película', to='AppCoder.generos')),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tipos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('descripcion', models.CharField(max_length=150)),
                ('imagen', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Preguntas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pregunta_usuario', models.IntegerField()),
                ('pregunta_texto', models.CharField(max_length=254)),
                ('pregunta_cuando', models.DateTimeField(auto_now_add=True)),
                ('respuesta_texto', models.CharField(max_length=254)),
                ('respuesta_cuando', models.DateTimeField(null=True)),
                ('mostrar', models.BooleanField()),
                ('pelicula', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='AppCoder.peliculas')),
            ],
        ),
        migrations.AddField(
            model_name='peliculas',
            name='tags',
            field=models.ManyToManyField(help_text='Etiquetas', to='AppCoder.tags'),
        ),
    ]
