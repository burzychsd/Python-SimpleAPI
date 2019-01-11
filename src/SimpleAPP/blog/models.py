from django.db import models
from django.urls import reverse

# Create your models here.
class Article(models.Model):
	author		= models.CharField(max_length=60)
	title       = models.CharField(max_length=60)
	description = models.CharField(max_length=60)
	content		= models.TextField()
	date		= models.DateField(auto_now=True)

	def get_absolute_url(self):
		return reverse('blog:article-detail', kwargs={'id': self.id})

	def get_create_url():
		return reverse('blog:article-create')

	def get_delete_url(self):
		return reverse('blog:article-delete', kwargs={'id': self.id})

	def get_update_url(self):
		return reverse('blog:article-update', kwargs={'id': self.id})