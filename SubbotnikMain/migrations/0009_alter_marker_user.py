# Generated by Django 5.0.1 on 2024-01-13 17:00

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SubbotnikMain', '0008_alter_marker_latitude_alter_marker_longitude'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marker',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='name'),
        ),
    ]
