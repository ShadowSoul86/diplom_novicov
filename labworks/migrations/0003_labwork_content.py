# Generated by Django 5.0.6 on 2024-06-01 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("labworks", "0002_alter_labwork_image_alter_labwork_slug"),
    ]

    operations = [
        migrations.AddField(
            model_name="labwork",
            name="content",
            field=models.TextField(default=""),
        ),
    ]