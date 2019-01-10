from django.db import models

# Create your models here.
class Comment(models.Model):
	author 	= models.CharField(max_length=80)
	text 	= models.TextField()
	date	= models.DateField(auto_now=True)