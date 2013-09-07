from django.db import models

class Prize(models.Model):
  name = models.CharField(max_length=200)
  value = models.IntegerField(default=0)
  sponsor = models.ForeignKey('Sponsor')

class Technology(models.Model):
  name = models.CharField(max_length=200)
  url = models.URLField(max_length=200)
  sponsor = models.ForeignKey('Sponsor')

class Sponsor(models.Model):
  name = models.CharField(max_length=200)
