# Generated by Django 3.2.17 on 2023-02-08 18:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_userprofile_balance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='username',
        ),
    ]