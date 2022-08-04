from django.contrib import admin
from core.models import Evento, Movie

# Register your models here.


class EventoAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'data_evento', 'data_criacao')
    list_filter = ('data_evento', 'usuario',)


admin.site.register(Evento, EventoAdmin)


class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'desc')
    list_filter = ('title',)


admin.site.register(Movie, MovieAdmin)
