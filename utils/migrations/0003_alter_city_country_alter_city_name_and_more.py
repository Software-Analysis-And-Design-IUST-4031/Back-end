# Generated by Django 5.1.3 on 2024-12-14 06:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0002_remove_city_iso3_code'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='country',
            field=models.CharField(db_index=True, default='Iran', max_length=100),
        ),
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(db_index=True, default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='userselection',
            name='city',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='userselection',
            name='country',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='userselection',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
