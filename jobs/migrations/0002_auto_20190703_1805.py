# Generated by Django 2.0.2 on 2019-07-03 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='jobs',
            new_name='Job',
        ),
    ]
