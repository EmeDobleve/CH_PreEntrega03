from argparse import _AppendAction
from django.db import models
from datetime import date

# Create your models here.

#documental, Ciencia Ficción, Policial, Thriller, comedia, romántica
class Generos(models.Model):
    nombre = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=250)
    #imagen = models.CharField(max_length=60)
    imagen = models.ImageField(
            upload_to='imgs/cat/'
            , height_field=None
            , width_field=None
            , max_length=100
    )

    def __str__(self):
        return f"{self.nombre}"     

#serie, pelicula, miniserie, dibujos animados, animacion computada
class Tipos(models.Model): 
        nombre = models.CharField(max_length=40)
        descripcion = models.CharField(max_length=150)
        imagen = models.ImageField(
                upload_to='imgs/tip/'
                , height_field=None
                , width_field=None
                , max_length=100
        )
        
        def __str__(self):
                return f"{self.nombre}"


class Directores(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100, default="Sin Apellido")
    foto = models.ImageField(
            upload_to='imgs/dir/'
            , height_field=None
            , width_field=None
            , max_length=100
            , default="imgs/defaults/dirSinFoto.jpg"
    )

    def __str__(self):
        return f"{self.nombre} {self.apellido}"        

class Acts(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)    
    foto = models.ImageField(
            upload_to='imgs/act/'
            , height_field=None
            , width_field=None
            , max_length=100
            , default="imgs/defaults/actSinFoto.jpg"
    )

    def __str__(self):
        return f"{self.nombre} {self.apellido}"        


#Etiquetas para las recomendaciones para poder navegarlas después
class Tags(models.Model):
        tag = models.CharField(max_length=50)

        def __str__(self):
                return f"{self.tag}"    

#Películas recomendadas
class Peliculas(models.Model):
        nombre = models.CharField(max_length=120)
        portada = models.ImageField(
            upload_to='imgs/pel/'
            , height_field=None
            , width_field=None
            , max_length=100
            , default="imgs/defaults/pelSinFoto.jpg"
        )
        resumen = models.CharField(max_length=250)
        imdb_link = models.CharField(max_length=150)
        motivo_recomendacion = models.CharField(max_length=250)    
        director = models.ForeignKey(
            'Directores'
            , on_delete=models.RESTRICT
            , null=True
        )
        #act_destacados = models.ManyToManyField(
        #    Acts
        #    #, through='peliculas_act_destacados'
        #    , help_text="Género/s"
        #    #, on_delete=models.RESTRICT
        #)
        act_destacado = models.ForeignKey(
            'Acts'
            , on_delete=models.RESTRICT
            , null=True
        )
        anio = models.IntegerField()
        #generos = models.ManyToManyField(
        #    Generos
        #    #, through='peliculas_generos'
        #    #, on_delete=models.RESTRICT
        #    , help_text="Géneros de Película"
        #)
        genero = models.ForeignKey(
            'Generos'
            , on_delete=models.RESTRICT
            , null=True
        )
        #tags = models.ManyToManyField(
        #    Tags
        #    #, through='peliculas_tags'
        #    #, on_delete=models.RESTRICT
        #    , help_text="Etiquetas"
        #)
        tag = models.ForeignKey(
            'Tags'
            , on_delete=models.RESTRICT
            , null=True
        )
        valoracion = models.IntegerField(default=1)

        def __str__(self):
                return f"{self.nombre} ({self.anio})"    

