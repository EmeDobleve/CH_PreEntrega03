from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context, loader
from AppCoder.models import *
from .forms import GeneroForm, TipoForm, DirectorForm, ActForm, TagForm, PeliculaForm

# Create your views here.

def inicio(self):
        plantilla = loader.get_template("AppCoder/inicio.html")
        documento = plantilla.render()
        return HttpResponse(documento)

def generos(request):
        form = GeneroForm()
        generos = Generos.objects.all() #Profesor.objects.filter(nombre__icontains="P").all()
        return render(request, "AppCoder/generos.html", {"generos": generos, "form" : form})

def buscarGeneros(request):
        genero = request.GET["genero"]
        if (genero!=""):
                generos = Generos.objects.filter(nombre__icontains=genero) #buscar otros filtros en la documentacion de django
                if (len(generos)>0):
                        return render(request, "AppCoder/generos.html", {"generos": generos, "filtro": genero})
                else:
                        return render(request, "AppCoder/generos.html", {"generos": generos, "filtro": genero, "mensaje": "No se encontraron casos que se ajusten al filtro!"})        
        else:
                generos = Generos.objects.all() #Profesor.objects.filter(nombre__icontains="P").all()
                return render(request, "AppCoder/generos.html", {"generos": generos, "mensaje": "No se ingresó ningún dato para filtrar!"})
                

def crearGenero(request):
    if request.method == "POST":
        form = GeneroForm(request.POST, request.FILES)
        if form.is_valid():
                genero = Generos()
                genero.nombre = form.cleaned_data['nombre']
                genero.descripcion = form.cleaned_data['descripcion']
                genero.imagen = form.cleaned_data['imagen']                
                genero.save()
                form = GeneroForm()
                generos = Generos.objects.all() 
                return render(request, "AppCoder/generos.html", {"generos": generos, "mensaje":"Género dado de alta satisfactoriamente!"})
        else:
                formulario= GeneroForm(initial={"nombre":form.cleaned_data['nombre'], "descripcion":form.cleaned_data['descripcion']})
                return render(request, "AppCoder/crearGeneros.html", {"form": formulario, "mensaje":"Algo falló. Intente Nuevamnte."})              
    else:
        form = GeneroForm()
        generos = Generos.objects.all() 
        return render(request, "AppCoder/crearGeneros.html", {"generos": generos, "form" : form})
    

def editarGenero(request, id):
    genero=Generos.objects.get(id=id)
    if request.method=="POST":
        form= GeneroForm(request.POST, request.FILES)

        if (not(request.FILES and request.FILES['imagen'])):
                request.FILES["imagen"] = genero.imagen

        if form.is_valid():
                info=form.cleaned_data
                genero.nombre=info["nombre"]
                genero.descripcion=info["descripcion"]
                genero.imagen=info["imagen"]
                genero.save()
                generos=Generos.objects.all()
                form = GeneroForm()
                return render(request, "AppCoder/generos.html" ,{"generos":generos, "form": form, "mensaje": "Género editado correctamente"})
        else:
                formulario= GeneroForm(initial={"nombre":form.cleaned_data['nombre'], "descripcion":form.cleaned_data['descripcion']})
                return render(request, "AppCoder/editarGenero.html genero.id", {"form": formulario, "genero": genero, "mensaje":"Algo falló. Intente Nuevamnte."})              
    else:
        formulario= GeneroForm(initial={"nombre":genero.nombre, "descripcion":genero.descripcion, "imagen":genero.imagen})
        return render(request, "AppCoder/editarGenero.html", {"form": formulario, "genero": genero})

def eliminarGenero(request, id):
        genero=Generos.objects.get(id=id)
        genero.delete()
        generos=Generos.objects.all()
        form = GeneroForm()
        return render(request, "AppCoder/generos.html", {"generos": generos, "mensaje": "Género eliminado correctamente", "form": form})

def tipos(request):
        form = TipoForm()
        tipos = Tipos.objects.all() #Profesor.objects.filter(nombre__icontains="P").all()
        return render(request, "AppCoder/tipos.html", {"tipos": tipos, "form" : form})


def buscarTipos(request):
        tipo = request.GET["tipo"]
        if (tipo!=""):
                tipos = Tipos.objects.filter(nombre__icontains=tipo) #buscar otros filtros en la documentacion de django
                if (len(tipo)>0):
                        return render(request, "AppCoder/tipos.html", {"tipos": tipos, "filtro": tipo})
                else:
                        return render(request, "AppCoder/tipos.html", {"tipos": tipos, "filtro": tipo, "mensaje": "No se encontraron casos que se ajusten al filtro!"})        
        else:
                tipos = Tipos.objects.all() #Profesor.objects.filter(nombre__icontains="P").all()
                return render(request, "AppCoder/tipos.html", {"tipos": tipos, "mensaje": "No se ingresó ningún dato para filtrar!"})
                

def crearTipo(request):
    if request.method == "POST":
        form = TipoForm(request.POST, request.FILES)
        if form.is_valid():
                tipo = Tipos()
                tipo.nombre = form.cleaned_data['nombre']
                tipo.descripcion = form.cleaned_data['descripcion']
                tipo.imagen = form.cleaned_data['imagen']                
                tipo.save()
                form = TipoForm()
                tipos = Tipos.objects.all() 
                return render(request, "AppCoder/tipos.html", {"tipos": tipos, "mensaje":"Tipo dado de alta satisfactoriamente!"})
        else:
                formulario= TipoForm(initial={"nombre":form.cleaned_data['nombre'], "descripcion":form.cleaned_data['descripcion'], "imagen":form.cleaned_data['imagen']})
                return render(request, "AppCoder/crearTipos.html", {"form": formulario, "mensaje":"Algo falló. Intente Nuevamnte."})              
    else:
        form = TipoForm()
        tipos = Tipos.objects.all() 
        return render(request, "AppCoder/crearTipos.html", {"tipos": tipos, "form" : form})
    

def editarTipo(request, id):
    tipo=Tipos.objects.get(id=id)
    if request.method=="POST":
        form= TipoForm(request.POST, request.FILES)

        if (not(request.FILES and request.FILES['imagen'])):
              request.FILES["imagen"] = tipo.imagen

        if form.is_valid():
                info=form.cleaned_data
                tipo.nombre=info["nombre"]
                tipo.descripcion=info["descripcion"]
                tipo.imagen=info["imagen"]
                tipo.save()
                tipos=Tipos.objects.all()
                form = TipoForm()
                return render(request, "AppCoder/tipos.html" ,{"tipos":tipos, "form": form, "mensaje": "Tipo editado correctamente"})
        else:
                formulario= TipoForm(initial={"nombre":form.cleaned_data['nombre'], "descripcion":form.cleaned_data['descripcion']})
                return render(request, "AppCoder/editarTipo.html tipo.id", {"form": formulario, "tipo": tipo, "mensaje":"Algo falló. Intente Nuevamnte."})              
    else:
        formulario= TipoForm(initial={"nombre":tipo.nombre, "descripcion":tipo.descripcion, "imagen":tipo.imagen})
        return render(request, "AppCoder/editarTipo.html", {"form": formulario, "tipo": tipo})

def eliminarTipo(request, id):
        tipo=Tipos.objects.get(id=id)
        tipo.delete()
        tipos=Tipos.objects.all()
        form = TipoForm()
        return render(request, "AppCoder/tipos.html", {"tipos": tipos, "mensaje": "Tipo eliminado correctamente", "form": form})


def directores(request):
        form = DirectorForm()
        directores = Directores.objects.all() #Profesor.objects.filter(nombre__icontains="P").all()
        return render(request, "AppCoder/directores.html", {"directores": directores, "form" : form})


def buscarDirectores(request):
        director = request.GET["director"]
        if (director!=""):
                directores = Directores.objects.filter(apellido__icontains=director) #buscar otros filtros en la documentacion de django
                if (len(directores)>0):
                        return render(request, "AppCoder/directores.html", {"directores": directores, "filtro": director})
                else:
                        return render(request, "AppCoder/directores.html", {"directores": directores, "filtro": director, "mensaje": "No se encontraron casos que se ajusten al filtro!"})        
        else:
                directores = Directores.objects.all() #Profesor.objects.filter(nombre__icontains="P").all()
                return render(request, "AppCoder/directores.html", {"directores": directores, "mensaje": "No se ingresó ningún dato para filtrar!"})
                

def crearDirector(request):
    if request.method == "POST":
        form = DirectorForm(request.POST, request.FILES)
        if form.is_valid():
                director = Directores()
                director.nombre = form.cleaned_data['nombre']
                director.apellido = form.cleaned_data['apellido']
                director.foto = form.cleaned_data['foto']                
                director.save()
                form = DirectorForm()
                directores = Directores.objects.all() 
                return render(request, "AppCoder/directores.html", {"directores": directores, "mensaje":"Director dado de alta satisfactoriamente!"})
        else:
                formulario= DirectorForm(initial={"nombre":form.cleaned_data['nombre'], "apellido":form.cleaned_data['apellido']})
                return render(request, "AppCoder/crearDirectores.html", {"form": formulario, "mensaje":"Algo falló. Intente Nuevamnte."})              
    else:
        form = DirectorForm()
        directores = Directores.objects.all() 
        return render(request, "AppCoder/crearDirectores.html", {"directores": directores, "form" : form})
    

def editarDirector(request, id):
    director=Directores.objects.get(id=id)
    if request.method=="POST":
        form= DirectorForm(request.POST, request.FILES)

        if (not(request.FILES and request.FILES['foto'])):
              request.FILES["foto"] = director.foto
              
        if form.is_valid():
                director.nombre=form.cleaned_data["nombre"]
                director.apellido=form.cleaned_data["apellido"]
                if (form.cleaned_data["foto"]!= ''):
                        director.foto=form.cleaned_data["foto"]
                director.save()
                directores=Directores.objects.all()
                form = DirectorForm()
                return render(request, "AppCoder/directores.html" ,{"directores":directores, "form": form, "mensaje": "Director editado correctamente"})
        else:
                formulario= DirectorForm(initial={"nombre":form.cleaned_data['nombre'], "apellido":form.cleaned_data['apellido']})
                return render(request, "AppCoder/editarDirector.html", {"form": formulario, "director": director, "mensaje":"Algo falló. Intente Nuevamnte."})              
    else:
        formulario= DirectorForm(initial={"nombre":director.nombre, "apellido":director.apellido, "foto":director.foto})
        return render(request, "AppCoder/editarDirector.html", {"form": formulario, "director": director})

def eliminarDirector(request, id):
        director=Directores.objects.get(id=id)
        director.delete()
        directores=Directores.objects.all()
        form = DirectorForm()
        return render(request, "AppCoder/directores.html", {"directores": directores, "mensaje": "Director eliminado correctamente", "form": form})


def acts(request):
        form = ActForm()
        acts = Acts.objects.all() #Profesor.objects.filter(nombre__icontains="P").all()
        return render(request, "AppCoder/acts.html", {"acts": acts, "form" : form})


def buscarActs(request):
        act = request.GET["act"]
        if (act!=""):
                acts = Acts.objects.filter(apellido__icontains=act) #buscar otros filtros en la documentacion de django
                if (len(acts)>0):
                        return render(request, "AppCoder/acts.html", {"acts": acts, "filtro": act})
                else:
                        return render(request, "AppCoder/acts.html", {"acts": acts, "filtro": act, "mensaje": "No se encontraron casos que se ajusten al filtro!"})        
        else:
                acts = Acts.objects.all() #Profesor.objects.filter(nombre__icontains="P").all()
                return render(request, "AppCoder/acts.html", {"acts": acts, "mensaje": "No se ingresó ningún dato para filtrar!"})
                

def crearAct(request):
    if request.method == "POST":
        form = ActForm(request.POST, request.FILES)
        if form.is_valid():
                act = Acts()
                act.nombre = form.cleaned_data['nombre']
                act.apellido = form.cleaned_data['apellido']
                act.foto = form.cleaned_data['foto']                
                act.save()
                form = ActForm()
                acts = Acts.objects.all() 
                return render(request, "AppCoder/acts.html", {"acts": acts, "mensaje":"Actriz o Actor dado de alta satisfactoriamente!"})
        else:
                formulario= ActForm(initial={"nombre":form.cleaned_data['nombre'], "apellido":form.cleaned_data['apellido']})
                return render(request, "AppCoder/crearActs.html", {"form": formulario, "mensaje":"Algo falló. Intente Nuevamnte."})              
    else:
        form = ActForm()
        acts = Acts.objects.all() 
        return render(request, "AppCoder/crearActs.html", {"acts": acts, "form" : form})


def editarAct(request, id):
    act=Acts.objects.get(id=id)
    if request.method=="POST":
        form= ActForm(request.POST, request.FILES)

        if (not(request.FILES and request.FILES['foto'])):
              request.FILES["foto"] = act.foto
              
        if form.is_valid():
                act.nombre=form.cleaned_data["nombre"]
                act.apellido=form.cleaned_data["apellido"]
                act.foto=form.cleaned_data["foto"]
                act.save()
                acts=Acts.objects.all()
                form = ActForm()
                return render(request, "AppCoder/acts.html" ,{"acts":acts, "form": form, "mensaje": "Artista editado correctamente"})
        else:
                formulario= ActForm(initial={"nombre":form.cleaned_data['nombre'], "apellido":form.cleaned_data['apellido']})
                return render(request, "AppCoder/editarAct.html", {"form": formulario, "act": act, "mensaje":"Algo falló. Intente Nuevamnte."})              
    else:
        formulario= ActForm(initial={"nombre":act.nombre, "apellido":act.apellido, "foto":act.foto})
        return render(request, "AppCoder/editarAct.html", {"form": formulario, "act": act})

def eliminarAct(request, id):
        act=Acts.objects.get(id=id)
        act.delete()
        acts=Acts.objects.all()
        form = ActForm()
        return render(request, "AppCoder/acts.html", {"acts": acts, "mensaje": "Artista eliminado correctamente", "form": form})


def tags(request):
        form = TagForm()
        tags = Tags.objects.all() #Profesor.objects.filter(nombre__icontains="P").all()
        return render(request, "AppCoder/tags.html", {"tags": tags, "form" : form})


def buscarTags(request):
        tag = request.GET["tag"]
        if (tag!=""):
                tags = Tags.objects.filter(tag__icontains=tag) #buscar otros filtros en la documentacion de django
                if (len(tags)>0):
                        return render(request, "AppCoder/tags.html", {"tags": tags, "filtro": tag})
                else:
                        return render(request, "AppCoder/tags.html", {"tags": tags, "filtro": tag, "mensaje": "No se encontraron casos que se ajusten al filtro!"})        
        else:
                tags = Tags.objects.all() #Profesor.objects.filter(nombre__icontains="P").all()
                return render(request, "AppCoder/tags.html", {"tags": tags, "mensaje": "No se ingresó ningún dato para filtrar!"})
                

def crearTag(request):
    if request.method == "POST":
        form = TagForm(request.POST)
        if form.is_valid():
                tag = Tags()
                tag.tag = form.cleaned_data['tag']
                tag.save()
                form = TagForm()
                tags = Tags.objects.all() 
                return render(request, "AppCoder/tags.html", {"tags": tags, "mensaje":"Tag dado de alta satisfactoriamente!"})
        else:
                formulario= TagForm(initial={"tag":form.cleaned_data['tag']})
                return render(request, "AppCoder/crearTags.html", {"form": formulario, "mensaje":"Algo falló. Intente Nuevamnte."})              
    else:
        form = TagForm()
        tags = Tags.objects.all() 
        return render(request, "AppCoder/crearTags.html", {"tags": tags, "form" : form})
    

def editarTag(request, id):
    tag=Tags.objects.get(id=id)
    if request.method=="POST":
        form= TagForm(request.POST)
        if form.is_valid():
                tag.tag=form.cleaned_data["tag"]
                tag.save()
                tags=Tags.objects.all()
                form = TagForm()
                return render(request, "AppCoder/tags.html" ,{"tags":tags, "form": form, "mensaje": "Tag editado correctamente"})
        else:
                formulario= TagForm(initial={"tag":form.cleaned_data['tag']})
                return render(request, "AppCoder/editarTag.html", {"form": formulario, "tag": tag, "mensaje":"Algo falló. Intente Nuevamnte."})              
    else:
        formulario= TagForm(initial={"tag":tag.tag})
        return render(request, "AppCoder/editarTag.html", {"form": formulario, "tag": tag})

def eliminarTag(request, id):
        tag=Tags.objects.get(id=id)
        tag.delete()
        tags=Tags.objects.all()
        form = TagForm()
        return render(request, "AppCoder/tags.html", {"tags": tags, "mensaje": "Tag eliminado correctamente", "form": form})


def peliculas(request):
        form = PeliculaForm()
        peliculas = Peliculas.objects.all() #Profesor.objects.filter(nombre__icontains="P").all()
        return render(request, "AppCoder/peliculas.html", {"peliculas": peliculas, "form" : form})


def buscarPeliculas(request):
        pelicula = request.GET["pelicula"]
        if (pelicula!=""):
                peliculas = Peliculas.objects.filter(nombre__icontains=pelicula) #buscar otros filtros en la documentacion de django
                if (len(peliculas)>0):
                        return render(request, "AppCoder/peliculas.html", {"peliculas": peliculas, "filtro": pelicula})
                else:
                        return render(request, "AppCoder/peliculas.html", {"peliculas": peliculas, "filtro": pelicula, "mensaje": "No se encontraron casos que se ajusten al filtro!"})        
        else:
                peliculas = Peliculas.objects.all() #Profesor.objects.filter(nombre__icontains="P").all()
                return render(request, "AppCoder/peliculas.html", {"peliculas": peliculas, "mensaje": "No se ingresó ningún dato para filtrar!"})
                

def crearPelicula(request):
    if request.method == "POST":
        form = PeliculaForm(request.POST, request.FILES)
        if form.is_valid():
                pelicula = Peliculas()
                pelicula.nombre = form.cleaned_data['nombre']
                pelicula.resumen = form.cleaned_data['resumen']
                pelicula.portada = form.cleaned_data['portada']   
                pelicula.imdb_link = form.cleaned_data['imdb_link']
                pelicula.motivo_recomendacion = form.cleaned_data['motivo_recomendacion']
                pelicula.anio = form.cleaned_data['anio']
                pelicula.valoracion = form.cleaned_data['valoracion']

                director=Directores.objects.get(id=request.POST.get("director"))
                pelicula.director =director

                act=Acts.objects.get(id=request.POST.get("act_destacado"))
                pelicula.act_destacado = act

                genero=Generos.objects.get(id=request.POST.get("genero"))
                pelicula.genero = genero

                tag=Tags.objects.get(id=request.POST.get("tag"))
                pelicula.tag = tag

                pelicula.save()

                form = PeliculaForm()
                peliculas = Peliculas.objects.all() 
                return render(request, "AppCoder/peliculas.html", {"peliculas": peliculas, "mensaje":"Pelicula dado de alta satisfactoriamente!"})
        else:
                formulario= PeliculaForm(initial={
                        "nombre":form.cleaned_data['nombre']
                        , "resumen" : form.cleaned_data['resumen']
                        , "portada" : form.cleaned_data['portada']   
                        , "imdb_link" : form.cleaned_data['imdb_link']
                        , "motivo_recomendacion" : form.cleaned_data['motivo_recomendacion']
                        , "director" : form.cleaned_data['director']   
                        , "act_destacado" : form.cleaned_data['act_destacado']
                        , "anio" : form.cleaned_data['anio']
                        , "genero" : form.cleaned_data['genero']   
                        , "tag" : form.cleaned_data['tag']
                        , "valoracion" : form.cleaned_data['valoracion']                        
                })
                return render(request, "AppCoder/crearPeliculas.html", {"form": formulario, "mensaje":"Algo falló. Intente Nuevamnte."})              
    else:
        form = PeliculaForm()
        peliculas = Peliculas.objects.all() 
        return render(request, "AppCoder/crearPeliculas.html", {"peliculas": peliculas, "form" : form})
    

def editarPelicula(request, id):
    pelicula=Peliculas.objects.get(id=id)
    if request.method=="POST":
        form= PeliculaForm(request.POST, request.FILES)

        if (not(request.FILES and request.FILES['portada'])):
              request.FILES["portada"] = pelicula.portada
              
        if form.is_valid():
                pelicula.nombre = form.cleaned_data['nombre']
                pelicula.resumen = form.cleaned_data['resumen']

                if (form.cleaned_data["portada"]!= ''):
                        pelicula.portada=form.cleaned_data["portada"]

                pelicula.imdb_link = form.cleaned_data['imdb_link']
                pelicula.motivo_recomendacion = form.cleaned_data['motivo_recomendacion']
                pelicula.anio = form.cleaned_data['anio']
                pelicula.valoracion = form.cleaned_data['valoracion']

                director=Directores.objects.get(id=request.POST.get("director"))
                pelicula.director =director

                act=Acts.objects.get(id=request.POST.get("act_destacado"))
                pelicula.act_destacado = act

                genero=Generos.objects.get(id=request.POST.get("genero"))
                pelicula.genero = genero

                tag=Tags.objects.get(id=request.POST.get("tag"))
                pelicula.tag = tag

                pelicula.save()

                peliculas=Peliculas.objects.all()
                form = PeliculaForm()
                return render(request, "AppCoder/peliculas.html" ,{"peliculas":peliculas, "form": form, "mensaje": "Pelicula editada correctamente"})
        else:
                formulario= PeliculaForm(initial={
                        "nombre":form.cleaned_data['nombre']
                        , "resumen" : form.cleaned_data['resumen']
                        , "portada" : form.cleaned_data['portada']   
                        , "imdb_link" : form.cleaned_data['imdb_link']
                        , "motivo_recomendacion" : form.cleaned_data['motivo_recomendacion']
                        , "director" : form.cleaned_data['director']   
                        , "act_destacado" : form.cleaned_data['act_destacado']
                        , "anio" : form.cleaned_data['anio']
                        , "genero" : form.cleaned_data['genero']   
                        , "tag" : form.cleaned_data['tag']
                        , "valoracion" : form.cleaned_data['valoracion']                        
                })                
                return render(request, "AppCoder/editarPelicula.html", {"form": formulario, "pelicula": pelicula, "mensaje":"Algo falló. Intente Nuevamnte."})              
    else:
        formulario= PeliculaForm(initial={
                "nombre":       pelicula.nombre
                , "resumen" : pelicula.resumen
                , "portada" : pelicula.portada
                , "imdb_link" : pelicula.imdb_link
                , "motivo_recomendacion" : pelicula.motivo_recomendacion
                , "director" : pelicula.director
                , "act_destacado" : pelicula.act_destacado
                , "anio" : pelicula.anio
                , "genero" : pelicula.genero
                , "tag" : pelicula.tag
                , "valoracion" : pelicula.valoracion
        })
        return render(request, "AppCoder/editarPelicula.html", {"form": formulario, "pelicula": pelicula})


def eliminarPelicula(request, id):
        pelicula=Peliculas.objects.get(id=id)
        pelicula.delete()
        peliculas=Peliculas.objects.all()
        form = PeliculaForm()
        return render(request, "AppCoder/peliculas.html", {"peliculas": peliculas, "mensaje": "Pelicula eliminada correctamente", "form": form})


