# Generated by Django 5.0.6 on 2024-06-01 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "lectures",
            "0002_remove_lecture_image_lecture_image1_lecture_image2_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="lecture",
            name="content",
            field=models.TextField(default=""),
            preserve_default=False,
        ),
    ]
