# Generated by Django 3.1.7 on 2021-03-07 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20210307_1344'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='mentors',
            field=models.ManyToManyField(to='api.Member'),
        ),
    ]
