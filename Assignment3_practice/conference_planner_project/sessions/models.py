from django.db import models

class Session(models.Model):
    title = models.CharField(max_length=200)
    speaker = models.CharField(max_length=100)
    start_time = models.TimeField()
    end_time = models.TimeField()
    room = models.CharField(max_length=100)
    description = models.TextField(max_length=300)

    def __str__(self):
        return self.title
