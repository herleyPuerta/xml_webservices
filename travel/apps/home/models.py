from django.db import models

# Create your models here.

class Categoria(models.Model):
	def url(self,filename):
		ruta = "images/categorias/%s/%s"%(self.nombre,filename)
		return ruta
	id_root		= models.IntegerField()
	nombre		= models.CharField(max_length=100)
	imagen		= models.ImageField(upload_to=url,null=True,blank=True)

	def __unicode__(self):
		return self.nombre

class Subcategoria(models.Model):
	nombre		= models.CharField(max_length=100)
	def __unicode__(self):
		return self.nombre

class Sitio(models.Model):
	def url(self,filename):
		ruta = "images/sitios/%s/%s"%(self.nombre,filename)
		return ruta
	nombre		= models.CharField(max_length=100)
	imagen		= models.ImageField(upload_to=url,null=True,blank=True)

	def __unicode__(self):
		return self.nombre


