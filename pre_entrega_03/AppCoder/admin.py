from django.contrib import admin
# Register your models here.
from .models import Generos,Tipos,Directores,Acts,Tags,Peliculas

# Register your models here.
admin.site.register(Generos)
admin.site.register(Tipos)
admin.site.register(Directores)
admin.site.register(Acts)
admin.site.register(Tags)
admin.site.register(Peliculas)
