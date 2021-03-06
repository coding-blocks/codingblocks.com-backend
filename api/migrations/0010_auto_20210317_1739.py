# Generated by Django 3.1.7 on 2021-03-17 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_course_mentors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='bg_color',
            field=models.CharField(choices=[('blue-light', 'Blue Light'), ('blue-dark', 'Blue Dark'), ('blue', 'Blue'), ('green-light', 'Green Light'), ('green-dark', 'Green Dark'), ('green', 'Green'), ('orange-light', 'Orange Light'), ('orange-dark', 'Orange Dark'), ('orange', 'Orange'), ('pink-light', 'Pink Light'), ('pink-dark', 'Pink Dark'), ('pink', 'Pink'), ('purple-light', 'Purple Light'), ('purple-dark', 'Purple Dark'), ('purple', 'Purple')], default='blue-light', max_length=200),
        ),
    ]
