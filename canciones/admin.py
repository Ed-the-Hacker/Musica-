from django.contrib import admin
from .models import Autores, Canciones

# Register your models here.
@admin.register(Autores)
class AutoresAdmin(admin.ModelAdmin):
    list_display = ('id', 'Nombre', 'Edad', 'Nacionalidad', 'FechaDeNacimiento')

@admin.register(Canciones)
class PreciosAdmin(admin.ModelAdmin):
    list_display = ('id', 'Titulo', 'Autor', 'FechaLanzamiento')