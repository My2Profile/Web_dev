from django.db import models

# Create your models here.


class Movie(models.Model):
	
	title = models.CharField(max_length=100, unique=True)
	director = models.CharField(max_length=100)
	year = models.DateField()
	rating = models.FloatField()

	def __str__(self):
		return self.title




class Genre(models.Model):

	name = models.CharField(max_length=100)
	description = models.TextField(blank=True, null=True)

