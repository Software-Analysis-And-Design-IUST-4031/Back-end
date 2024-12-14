# Generated by Django 5.1.4 on 2024-12-14 08:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("painting", "0002_like_painting_like_user_painting_artist_and_more"),
        ("registering", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="cover_painting",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="galleries_as_cover",
                to="painting.painting",
            ),
        ),
    ]