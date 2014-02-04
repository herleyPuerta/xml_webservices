from django.http import HttpResponse
from travel.apps.home.models import Categoria, Subcategoria, Sitio
from django.template.loader import render_to_string
from django.core import serializers



def categories_xml_view(request):
	categorias = Categoria.objects.filter(id_root=0)
	xml = render_to_string('xml_category_template.xml', {'query_set': categorias})
	return HttpResponse(xml,mimetype="application/xml")

def subcategories_restaurant_xml_view(request):
	subcategorias = Categoria.objects.filter(id_root=2)
	xml = render_to_string('xml_category_restaurant_template.xml', {'query_set': categorias})
	return HttpResponse(xml,mimetype="application/xml")


"""

def categories_xml_view(request):
	data = serializers.serialize("xml",Categoria.objects.all())
	#retorna la informacion en formato json
	return HttpResponse(data,mimetype="application/xml")


"""

def subcategories_xml_view(request):
	subcategorias = Subcategoria.objects.all()
	xml = render_to_string('xml_subcategory_template.xml', {'query_set': subcategorias})
	return HttpResponse(xml,mimetype="application/xml")

def sites_xml_view(request):
	sitios = Sitio.objects.all()
	xml = render_to_string('xml_site_template.xml', {'query_set': sitios})
	return HttpResponse(xml,mimetype="application/xml")
