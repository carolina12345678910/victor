from django.db import models

# Create your models here.
class Portada(models.Model):
	titulo = models.CharField(max_length=60)
	foto = models.ImageField(upload_to='imagenes/')


	def __str__(self):
		return self.titulo

class Portada_dos(models.Model):
	titulo = models.CharField(max_length=60)
	imagen = models.ImageField(upload_to='imagenes/')

	def __str__(self):
		return self.titulo
		
portada = Portada('portada')

class CorteMujer(models.Model):
	precio = models.CharField(max_length=60)
	especificacion = models.CharField(max_length=300)


	def __str__(self):
		return self.precio

class Info_Color(models.Model):
	titulo = models.CharField(max_length=60)
	informacion = models.TextField(max_length=300)
	imagen = models.ImageField(upload_to='imagenes/')

	def __str__(self):
		return self.titulo


class Horario(models.Model):
	titulo = models.CharField(max_length=60)
	imagen = models.ImageField(upload_to='imagenes/')

	def __str__(self):
		return self.titulo

class Trabajos(models.Model):
	nombre = models.CharField(max_length=60)
	foto = models.ImageField(upload_to='imagenes/')

	def __str__(self):
		return self.nombre

class Recomendaciones(models.Model):
	nombre = models.CharField(max_length=60)
	imagen = models.ImageField(upload_to='imagenes/')
	especificacion = models.TextField(max_length=900)

	def __str__(self):
		return self.nombre

class Promociones(models.Model):
	tipo = models.CharField(max_length=60)
	diseño = models.ImageField(upload_to='imagenes/')

	def __str__(self):
		return self.tipo
		