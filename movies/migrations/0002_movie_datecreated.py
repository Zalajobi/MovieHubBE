# Generated by Django 3.2.7 on 2021-09-20 08:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='dateCreated',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
