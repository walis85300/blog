from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Post(models.Model):
	
	autor = models.ForeignKey(User)
	titulo = models.CharField(max_length=50,unique=True)
	resumen = models.CharField(max_length=100,unique=True)
	contenido = models.TextField()
	fecha_creacion = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.titulo.capitalize()
