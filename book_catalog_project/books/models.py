from django.db import models

# Create your models here.

class Genre(models.Model):

	name = models.CharField(max_length=100, unique=True)
	description = models.TextField(blank=True, null=True)

	def __str__(self):
		return self.name



class Book(models.Model):

	title = models.CharField(max_length=200)
	author = models.CharField(max_length=150)
	publication_year = models.IntegerField()
	price = models.DecimalField(max_digits=5, decimal_places=2)
	genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

	def __str__(self):
		return self.title


