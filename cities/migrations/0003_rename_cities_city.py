# Generated by Django 3.2.17 on 2023-02-10 12:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0002_alter_cities_city'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cities',
            new_name='City',
        ),
    ]
