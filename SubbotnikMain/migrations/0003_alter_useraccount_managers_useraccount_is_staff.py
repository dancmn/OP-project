# Generated by Django 5.0.1 on 2024-01-13 10:02

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SubbotnikMain', '0002_remove_marker_pollutionlevel_and_more'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='useraccount',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='useraccount',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]
