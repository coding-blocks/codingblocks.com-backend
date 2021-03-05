from django.contrib.postgres.fields import ArrayField
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

class Company(models.Model):
    name = models.CharField(max_length=100,default='')
    logo = models.URLField(default='')
class SuccessStory(models.Model):
    title = models.CharField(max_length=200)
    subTitle = models.CharField(max_length=200)
    body = models.CharField(max_length=500)
    img = models.URLField()
    college = models.CharField(max_length=200)
    course = models.CharField(max_length=200)
    company = models.ForeignKey("Company", on_delete=models.CASCADE,null=True)

class Queries(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phoneNo = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    type = models.CharField(max_length=50)

class Course(models.Model):
    theme_choices = [
        ('theme-blue', 'blue'),
        ('theme-green', 'green'),
        ('theme-orange', 'orange'),
        ('theme-pink', 'pink'),
        ('theme-purple', 'purple'),
    ]
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=10000)
    logo = models.URLField()
    price = models.IntegerField()
    mrp = models.IntegerField()
    theme =  models.CharField(
        max_length=200,
        choices=theme_choices,
        default='theme-blue'
    )
    rating = models.IntegerField()
    number_ratings = models.IntegerField()
    slug = models.CharField(max_length=1000)
    start_day = models.DateField()
    registrations_open_day = models.DateField()
    video_link = models.URLField()
    languages = ArrayField(models.CharField(max_length=10, blank=True),size=2)
    duration = models.CharField(max_length=200)
    buy_link = models.URLField()


class Member(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    contact = models.EmailField(max_length=100)
    img = models.URLField()
    description = models.CharField(max_length=1000)


