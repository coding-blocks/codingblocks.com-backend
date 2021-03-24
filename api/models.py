from django.contrib.postgres.fields import ArrayField
from django.db import models

# Create your models here.
class MiniBanner(models.Model):
    tag = models.CharField(max_length=20)
    img_url = models.URLField(max_length=200)

    def __str__(self):
        return self.tag

class Banner(models.Model):
    bg_choices = [
        ('blue-light', 'Blue Light'),
        ('blue-dark', 'Blue Dark'),
        ('blue', 'Blue'),
        ('green-light', 'Green Light'),
        ('green-dark', 'Green Dark'),
        ('green', 'Green'),
        ('orange-light', 'Orange Light'),
        ('orange-dark', 'Orange Dark'),
        ('orange', 'Orange'),
        ('pink-light', 'Pink Light'),
        ('pink-dark', 'Pink Dark'),
        ('pink', 'Pink'),
        ('purple-light', 'Purple Light'),
        ('purple-dark', 'Purple Dark'),
        ('purple', 'Purple')
    ]

    tag = models.CharField(max_length=20)
    heading1 = models.CharField(max_length=200)
    heading2 = models.CharField(max_length=200)
    tagline = models.CharField(max_length=200)
    subText = models.CharField(max_length=200)
    img_url = models.URLField(max_length=200)
    cta = models.CharField(max_length=200)
    bg_color = models.CharField(
        max_length=200,
        choices=bg_choices,
        default='blue-light'
    )

    def __str__(self):
        return self.heading1

class Company(models.Model):
    name = models.CharField(max_length=100,default='')
    logo = models.URLField(default='')

    def __str__(self):
        return self.name


class SuccessStory(models.Model):
    name = models.CharField(max_length=200)
    lpa = models.IntegerField(default=0)
    subTitle = models.CharField(max_length=200)
    body = models.CharField(max_length=500)
    img = models.URLField()
    college = models.CharField(max_length=200)
    course = models.CharField(max_length=200)
    company = models.ForeignKey("Company", on_delete=models.CASCADE,null=True, related_name='success_stories')

    def __str__(self):
        return self.name

class Queries(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phoneNo = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Centre(models.Model):
    choices= [
        ('pitampura','Pitampura'),
        ('noida','Noida'),
        ('live','Live')
    ]
    name = models.CharField(
        max_length=50,
        choices=choices,
        default='noida'
    )

    def __str__(self):
        return self.name

class Batch(models.Model):
    buyLink = models.URLField()
    enrollmentStartDate = models.DateField()
    enrollmentEndDate = models.DateField()
    startDate = models.DateField()
    endDate = models.DateField()
    price = models.IntegerField()
    mrp = models.IntegerField()
    course = models.ForeignKey("Course", on_delete=models.CASCADE)
    centre = models.ForeignKey("Centre", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.centre) + " - " + str(self.course)

class Member(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    contact = models.EmailField(max_length=100)
    img = models.URLField()
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

class Course(models.Model):
    theme_choices = [
        ('theme-blue', 'blue'),
        ('theme-green', 'green'),
        ('theme-orange', 'orange'),
        ('theme-pink', 'pink'),
        ('theme-purple', 'purple'),
    ]
    difficulty_choices = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced')
    ]
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=10000)
    logo = models.URLField()
    theme =  models.CharField(
        max_length=200,
        choices=theme_choices,
        default='theme-blue'
    )
    rating = models.IntegerField()
    number_ratings = models.IntegerField()
    slug = models.CharField(max_length=1000)
    video_link = models.URLField()
    languages = ArrayField(models.CharField(max_length=10, blank=True),size=2)
    duration = models.CharField(max_length=200)
    difficulty = models.CharField(
        max_length=200,
        choices=difficulty_choices,
        default='beginner'
    )
    mentors = models.ManyToManyField(Member)
    projects =  models.JSONField()
    syallabus  = models.JSONField()
    highlights = models.JSONField()

    def __str__(self):
        return self.title



