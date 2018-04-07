from django.db import models

<<<<<<< HEAD
# Create your models here.
=======

class courses(models.Model):

	name = models.CharField('Nome', max_length=100)
	slug = models.SlugField('Atalho')
	description = models.TextField('Descricao', blank=True)
	start_date = models.DateField(
		'Data de Inicio', null=True, blank=True
	)
	image = models.ImageField(upload_to='courses/image', verbose_name='Imagem')

	created_at = models.DateTimeField(
		'Criado em', auto_now_add=True
	)
	updated_at = models.DateTimeField('Atualizado em', auto_now=True)
>>>>>>> 46ce90fe4035ea380c6e6b06ca8d29d0aacfcef6
