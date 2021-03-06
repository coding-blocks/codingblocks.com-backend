# Generated by Django 3.1.7 on 2021-03-05 11:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20210305_0957'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('logo', models.URLField(default='')),
            ],
        ),
        migrations.RemoveField(
            model_name='successstory',
            name='company_logo',
        ),
        migrations.RemoveField(
            model_name='successstory',
            name='company_name',
        ),
        migrations.AddField(
            model_name='successstory',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.company'),
        ),
    ]
