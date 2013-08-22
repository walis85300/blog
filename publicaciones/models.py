from django.db import models

# Create your models here.

class Post(models.Model):
	
	contenido = models.TextField()
	fecha_creacion = models.DateTimeField(auto_now=True)
	resumen = models.CharField(max_length=100,unique=True)
	titulo = models.CharField(max_length=50,unique=True)

	def __unicode__(self):
		return self.titulo.capitalize()
