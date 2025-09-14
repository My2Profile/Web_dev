from django.db import models

# Create your models here.

class Seans(models.Model):
	title = models.CharField(max_length=100)
	speaker = models.CharField(max_length=150)
	start_time = models.DateTimeField()
	end_time = models.DateTimeField()
	room = models.IntegerField()
	description = models.CharField(max_length=200)

	def __str__(self):
		return self.title
