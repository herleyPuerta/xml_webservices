from django.db import models

# Create your models here.

class Categoria(models.Model):
	def url(self,filename):
		ruta = "images/categorias/%s/%s"%(self.nombre,filename)
		return ruta
	id_root		= models.IntegerField()
	nombre		= models.CharField(max_length=100)
	imagen		= models.ImageField(upload_to=url,null=True,blank=True)

	def get_sitio(self):
		return Sitio.objects.filter(idCategoria=self)

	def __unicode__(self):
		return self.nombre

class Sitio(models.Model):
	def url(self,filename):
		ruta = "images/sitios/%s/%s"%(self.nombre,filename)
		return ruta
	idCategoria = models.ForeignKey(Categoria)
	nombre		= models.CharField(max_length=100)
	imagen		= models.ImageField(upload_to=url,null=True,blank=True)

	def __unicode__(self):
		return self.nombre


