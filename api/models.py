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

class SuccessStory(models.Model):
    title = models.CharField(max_length=200)
    subTitle = models.CharField(max_length=200)
    body = models.CharField(max_length=500)
    img = models.URLField()
    company_logo = models.URLField()
    company_name = models.CharField(max_length=200)
    college = models.CharField(max_length=200)
    course = models.CharField(max_length=200)
