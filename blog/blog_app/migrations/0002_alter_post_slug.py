# Generated by Django 5.0.6 on 2024-05-11 09:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog_app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="slug",
            field=models.SlugField(max_length=250, unique_for_date="publish"),
        ),
    ]
