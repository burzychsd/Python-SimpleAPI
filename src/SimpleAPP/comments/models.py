from django.db import models
from django.urls import reverse

# Create your models here.
class Comment(models.Model):
	author 	= models.CharField(max_length=80)
	text 	= models.TextField()
	date	= models.DateField(auto_now=True)

	def get_absolute_url(self):
		return reverse('comments:comment-detail', kwargs={'id': self.id})