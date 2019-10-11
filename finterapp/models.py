from django.db import models

# Create your models here.

class WordsModel(models.Model):
  word = models.CharField(max_length=255)
  frequency = models.IntegerField()