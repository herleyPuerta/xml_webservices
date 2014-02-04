from django.contrib import admin
from travel.apps.home.models import Categoria, Subcategoria, Sitio

class Categoria_Admin(admin.ModelAdmin):
	list_display = ('pk','id_root','nombre')

admin.site.register(Categoria,Categoria_Admin)
admin.site.register(Subcategoria)
admin.site.register(Sitio)