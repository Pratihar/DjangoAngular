# Generated by Django 2.0.5 on 2018-10-13 10:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='account',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='createdBy',
        ),
    ]
