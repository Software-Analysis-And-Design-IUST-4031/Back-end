# Generated by Django 5.1.3 on 2024-11-24 12:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('painting', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='painting',
            name='artist',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='paintings', to=settings.AUTH_USER_MODEL),
        ),
    ]