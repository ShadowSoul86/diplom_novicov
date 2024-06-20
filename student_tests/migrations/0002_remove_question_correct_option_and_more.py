# Generated by Django 5.0.6 on 2024-05-29 15:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("student_tests", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="question",
            name="correct_option",
        ),
        migrations.RemoveField(
            model_name="question",
            name="option1",
        ),
        migrations.RemoveField(
            model_name="question",
            name="option2",
        ),
        migrations.RemoveField(
            model_name="question",
            name="option3",
        ),
        migrations.RemoveField(
            model_name="question",
            name="option4",
        ),
        migrations.RemoveField(
            model_name="question",
            name="question_text",
        ),
        migrations.RemoveField(
            model_name="test",
            name="slug",
        ),
        migrations.RemoveField(
            model_name="testresult",
            name="student_name",
        ),
        migrations.AddField(
            model_name="question",
            name="text",
            field=models.TextField(default=""),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="question",
            name="image",
            field=models.FileField(blank=True, null=True, upload_to="question_images/"),
        ),
        migrations.AlterField(
            model_name="question",
            name="test",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="questions",
                to="student_tests.test",
            ),
        ),
        migrations.AlterField(
            model_name="testresult",
            name="test",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="results",
                to="student_tests.test",
            ),
        ),
    ]