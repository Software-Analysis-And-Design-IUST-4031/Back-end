# Generated by Django 5.1.3 on 2024-11-24 12:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('painting', '0002_painting_artist'),
        ('registering', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='cover_painting',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='galleries_as_cover', to='painting.painting'),
        ),
    ]
