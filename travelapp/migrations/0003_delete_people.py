# Generated by Django 3.2.7 on 2023-08-24 05:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0002_people'),
    ]

    operations = [
        migrations.DeleteModel(
            name='people',
        ),
    ]