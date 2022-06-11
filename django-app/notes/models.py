from django.db import models

class Note(models.Model):
    header = models.CharField(max_length=200)
    body = models.TextField()
