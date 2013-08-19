from django.db import models

# Create your models here.

class Post(models.Model):
	titulo = models.CharField(max_length=50,unique=True)
	contenido = models.TextField()
	fecha_creacion = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.titulo
