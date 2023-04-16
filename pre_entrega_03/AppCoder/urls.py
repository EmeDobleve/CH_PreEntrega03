from django.urls import path
from AppCoder.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', inicio),   
    path("Acts/", acts, name="Act"),
    path("Tags/", tags, name="Tag"),
    path("Peliculas/", peliculas, name="Pel"),

    path("Generos/",                    generos,            name="Gen"),    
    path("Generos/Buscar/",             buscarGeneros,      name="GenBus"),
    path("Generos/Eliminar/<id>",       eliminarGenero,     name="GenEli"),
    path("Generos/Editar/<id>",         editarGenero,       name="GenEdi"),
    path("Generos/Crear/",              crearGenero,        name="GenCre"),

    path("Tipos/",                      tipos,              name="Tip"),
    path("Tipos/Buscar/",               buscarTipos,        name="TipBus"),
    path("Tipos/Eliminar/<id>",         eliminarTipo,       name="TipEli"),
    path("Tipos/Editar/<id>",           editarTipo,         name="TipEdi"),
    path("Tipos/Crear/",                crearTipo,          name="TipCre"),  

    path("Directores/",                 directores,         name="Dir"),
    path("Directores/Buscar/",          buscarDirectores,   name="DirBus"),
    path("Directores/Eliminar/<id>",    eliminarDirector,   name="DirEli"),
    path("Directores/Editar/<id>",      editarDirector,     name="DirEdi"),
    path("Directores/Crear/",           crearDirector,      name="DirCre"),    

    path("Acts/", 			            acts, 		        name="Act"),
    path("Acts/Buscar/",                buscarActs,         name="ActBus"),
    path("Acts/Eliminar/<id>",          eliminarAct,        name="ActEli"),
    path("Acts/Editar/<id>",            editarAct,          name="ActEdi"),
    path("Acts/Crear/",                 crearAct,           name="ActCre"),      

    path("Tags/", 			            tags, 		        name="Tag"),
    path("Tags/Buscar/",                buscarTags,         name="TagBus"),
    path("Tags/Eliminar/<id>",          eliminarTag,        name="TagEli"),
    path("Tags/Editar/<id>",            editarTag,          name="TagEdi"),
    path("Tags/Crear/",                 crearTag,           name="TagCre"),      

    path("Peliculas/", 			        peliculas, 		    name="Pel"),
    path("Peliculas/Buscar/",           buscarPeliculas,    name="PelBus"),
    path("Peliculas/Eliminar/<id>",     eliminarPelicula,   name="PelEli"),
    path("Peliculas/Editar/<id>",       editarPelicula,     name="PelEdi"),
    path("Peliculas/Crear/",            crearPelicula,      name="PelCre"),      

]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)