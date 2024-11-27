# Generated by Django 5.1.3 on 2024-11-27 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Painting",
            fields=[
                ("painting_id", models.AutoField(primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=255)),
                ("description", models.TextField()),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="paintings/"),
                ),
                ("creation_date", models.DateField(auto_now_add=True)),
            ],
        ),
    ]
