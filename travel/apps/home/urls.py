from django.conf.urls import patterns, url

urlpatterns = patterns('travel.apps.home.views',
    url(r'^category/$', 'categories_xml_view', name='categorias'),
    url(r'^site/$', 'sites_xml_view', name='sitios'),
    url(r'^dataSite/$','get_site_view',name='getSiteInfo'),
    )