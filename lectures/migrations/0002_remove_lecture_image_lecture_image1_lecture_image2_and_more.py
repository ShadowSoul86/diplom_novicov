# Generated by Django 5.0.6 on 2024-05-29 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("lectures", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="lecture",
            name="image",
        ),
        migrations.AddField(
            model_name="lecture",
            name="image1",
            field=models.FileField(blank=True, null=True, upload_to="lecture_images/"),
        ),
        migrations.AddField(
            model_name="lecture",
            name="image2",
            field=models.FileField(blank=True, null=True, upload_to="lecture_images/"),
        ),
        migrations.AddField(
            model_name="lecture",
            name="image3",
            field=models.FileField(blank=True, null=True, upload_to="lecture_images/"),
        ),
        migrations.AddField(
            model_name="lecture",
            name="image4",
            field=models.FileField(blank=True, null=True, upload_to="lecture_images/"),
        ),
        migrations.AddField(
            model_name="lecture",
            name="image5",
            field=models.FileField(blank=True, null=True, upload_to="lecture_images/"),
        ),
        migrations.AddField(
            model_name="lecture",
            name="image6",
            field=models.FileField(blank=True, null=True, upload_to="lecture_images/"),
        ),
        migrations.AlterField(
            model_name="lecture",
            name="slug",
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
