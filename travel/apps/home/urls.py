from django.conf.urls import patterns, url

urlpatterns = patterns('travel.apps.home.views',
    url(r'^category/$', 'categories_xml_view', name='categorias'),
    url(r'^subcategory/$', 'subcategories_xml_view', name='subcategorias'),
    subcategories_restaurant_xml_view
    url(r'^restaurant/$', 'subcategories_restaurant_xml_view', name='restaurant'),
    url(r'^site/$', 'sites_xml_view', name='sitios'),
    )