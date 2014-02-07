from django.http import HttpResponse
from travel.apps.home.models import Categoria,Sitio
from django.template.loader import render_to_string
from django.core import serializers
#import xml.etree.ElementTree as ET
from xml.etree import cElementTree as ET

from lxml import objectify

import json
from django.views.decorators.csrf import csrf_exempt



def categories_xml_view(request):
	categorias = Categoria.objects.all()
	xml = render_to_string('xml_category_template.xml', {'query_set': categorias})
	return HttpResponse(xml,mimetype="application/xml")


def sites_xml_view(request):
	sitios = Sitio.objects.all()
	xml = render_to_string('xml_site_template.xml', {'query_set': sitios})
	return HttpResponse(xml,mimetype="application/xml")


@csrf_exempt
def get_site_view(request):
	xmlString = request.body
	x = objectify.fromstring(xmlString)
	identificador = x.idCategory
	sites = Sitio.objects.filter(idCategoria=identificador)
	xmlForTemplate = render_to_string('xml_site_id.xml',{'query_set':sites})	
	return HttpResponse(xmlForTemplate,mimetype="application/xml")
