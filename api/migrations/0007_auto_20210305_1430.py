# Generated by Django 3.1.7 on 2021-03-05 14:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_member'),
    ]

    operations = [
        migrations.CreateModel(
            name='Centre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('pitampura', 'Pitampura'), ('noida', 'Noida'), ('live', 'Live')], default='noida', max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='course',
            name='buy_link',
        ),
        migrations.RemoveField(
            model_name='course',
            name='mrp',
        ),
        migrations.RemoveField(
            model_name='course',
            name='price',
        ),
        migrations.RemoveField(
            model_name='course',
            name='registrations_open_day',
        ),
        migrations.RemoveField(
            model_name='course',
            name='start_day',
        ),
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buyLink', models.URLField()),
                ('enrollmentStartDate', models.DateField()),
                ('enrollmentEndDate', models.DateField()),
                ('startDate', models.DateField()),
                ('endDate', models.DateField()),
                ('price', models.IntegerField()),
                ('Mrp', models.IntegerField()),
                ('centre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.centre')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.course')),
            ],
        ),
    ]