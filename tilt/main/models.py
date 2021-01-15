from django.db import models

# Create your models here.

class illness(models.Model):
    name = models.CharField(max_length=200)
    symptoms = models.TextField(blank=False)
    description = models.TextField(blank=False)
    more = models.CharField(max_length=200, blank=True)