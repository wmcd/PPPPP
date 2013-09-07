from django.db import models

class Prize(models.Model):
  sponsor = models.ForeignKey('Sponsor')
  title = models.CharField(max_length=200)
  value = models.IntegerField(default=0)
  def __unicode__(self):
    return self.title

class Technology(models.Model):
  sponsor = models.ForeignKey('Sponsor')
  url = models.URLField(max_length=200)
  def __unicode__(self):
    return self.url

class Sponsor(models.Model):
  name = models.CharField(max_length=200, unique=True)
  def __unicode__(self):
    return self.name
