from django.db import models

# Create your models here.
class MiniBanner(models.Model):
    tag = models.CharField(max_length=20)
    img_url = models.URLField(max_length=200)


class Banner(models.Model):
    tag = models.CharField(max_length=20)
    heading1 = models.CharField(max_length=200)
    heading2 = models.CharField(max_length=200)
    tagline = models.CharField(max_length=200)
    subText = models.CharField(max_length=200)
    img_url = models.URLField(max_length=200)
    cta = models.CharField(max_length=200)
    bg_color = models.CharField(max_length=200)

