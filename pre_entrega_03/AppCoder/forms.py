from django import forms
from django.forms import ModelForm
from AppCoder.models import *

class GeneroForm(forms.Form):
    nombre = forms.CharField(max_length=40)
    descripcion = forms.CharField(max_length=250)
    imagen = forms.ImageField(max_length=100,allow_empty_file=False)

class TipoForm(forms.Form): 
    nombre = forms.CharField(max_length=40)
    descripcion = forms.CharField(max_length=150)
    imagen = forms.ImageField(max_length=100,allow_empty_file=False)

class DirectorForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    foto = forms.ImageField(max_length=100,allow_empty_file=False)

class ActForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)   
    foto = forms.ImageField(max_length=100,allow_empty_file=False)

#Etiquetas para las recomendaciones para poder navegarlas después
class TagForm(forms.Form):
    tag = forms.CharField(max_length=50)

#Películas recomendadas
class PeliculaForm(forms.Form):
        nombre = forms.CharField(max_length=120)
        portada = forms.ImageField(max_length=100,allow_empty_file=False)
        resumen = forms.CharField(max_length=250)
        imdb_link = forms.CharField(max_length=150)
        motivo_recomendacion = forms.CharField(max_length=250)    
        director = forms.ModelChoiceField(queryset=Directores.objects.all())
        act_destacado = forms.ModelChoiceField(queryset=Acts.objects.all())
        anio = forms.IntegerField()
        genero = forms.ModelChoiceField(queryset=Generos.objects.all())
        tag = forms.ModelChoiceField(queryset=Tags.objects.all())
        valoracion = forms.IntegerField(min_value=1, max_value=5)    
       