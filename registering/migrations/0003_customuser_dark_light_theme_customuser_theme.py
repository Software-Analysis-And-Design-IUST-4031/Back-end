# Generated by Django 5.1.3 on 2024-12-11 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registering', '0002_customuser_cover_painting'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='Dark_light_theme',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='Theme',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
