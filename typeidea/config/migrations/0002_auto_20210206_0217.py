# Generated by Django 2.2.13 on 2021-02-05 18:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='link',
            name='updated_time',
        ),
        migrations.RemoveField(
            model_name='sidebar',
            name='updated_time',
        ),
    ]
