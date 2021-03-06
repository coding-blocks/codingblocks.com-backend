# Generated by Django 3.1.7 on 2021-04-04 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_auto_20210402_1108'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventType', models.CharField(choices=[('workshop', 'Workshop'), ('contest', 'Contest'), ('other', 'Other')], default='workshop', max_length=100)),
                ('title', models.CharField(max_length=500)),
                ('slug', models.CharField(max_length=1000)),
                ('subject', models.CharField(max_length=1000)),
                ('description', models.CharField(max_length=2500)),
                ('registrationEndDate', models.DateField()),
                ('eventDate', models.DateField()),
                ('venue', models.CharField(max_length=200)),
                ('time', models.TimeField()),
                ('level', models.CharField(choices=[('beginner', 'Beginner'), ('intermediate', 'Intermediate'), ('advanced', 'Advanced')], default='beginner', max_length=200)),
                ('num_questions', models.IntegerField()),
                ('img_link', models.URLField()),
                ('mentors', models.ManyToManyField(to='api.Member')),
            ],
        ),
    ]
