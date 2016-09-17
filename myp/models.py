from __future__ import unicode_literals

from django.db import models
class Test(models.Model):
      name = models.CharField(max_length=20)
class Firstgroup(models.Model):
      name = models.CharField(max_length=20)
class Secondgroup(models.Model):
      name = models.CharField(max_length=20)
      firstgroup = models.ForeignKey(Firstgroup)
class Knowledgepoint(models.Model):
      secondgroup = models.ForeignKey(Secondgroup)
      name = models.CharField(max_length=20)
      description = models.CharField(max_length=150)
      url = models.CharField(max_length=10000)
      #type = models.IntegerField()

      
# Create your models here.
