# Generated by Django 3.1.7 on 2021-04-02 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_auto_20210330_0624'),
    ]

    operations = [
        migrations.AddField(
            model_name='successstory',
            name='placementType',
            field=models.CharField(choices=[('I', 'Internship'), ('P', 'Placement')], default='P', max_length=20),
        ),
        migrations.AlterField(
            model_name='queries',
            name='type',
            field=models.CharField(max_length=20),
        ),
    ]
