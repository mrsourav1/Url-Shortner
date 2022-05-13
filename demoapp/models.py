from django.db import models

# Create your models here.
class DemoUrl(models.Model):
    short_url = models.CharField(max_length = 100)
    long_url = models.URLField("URL")