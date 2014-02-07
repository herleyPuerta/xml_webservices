from django.contrib import admin
from travel.apps.home.models import Categoria, Sitio

class Categoria_Admin(admin.ModelAdmin):
	list_display = ('pk','id_root','nombre')

admin.site.register(Categoria,Categoria_Admin)
admin.site.register(Sitio)