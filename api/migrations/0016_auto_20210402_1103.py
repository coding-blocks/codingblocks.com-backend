# Generated by Django 3.1.7 on 2021-04-02 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_auto_20210402_1100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='successstory',
            name='subTitle',
            field=models.CharField(max_length=200, null=True),
        ),
    ]