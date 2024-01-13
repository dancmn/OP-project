# Generated by Django 5.0.1 on 2024-01-13 10:05

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SubbotnikMain', '0003_alter_useraccount_managers_useraccount_is_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marker',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='marker',
            name='signed',
            field=models.ManyToManyField(blank=True, related_name='markers', to=settings.AUTH_USER_MODEL),
        ),
    ]
