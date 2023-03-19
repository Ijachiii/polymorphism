# Generated by Django 4.1.7 on 2023-03-19 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bookstore", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="book",
            name="download_link",
        ),
        migrations.RemoveField(
            model_name="book",
            name="weight",
        ),
        migrations.AddField(
            model_name="book",
            name="extra",
            field=models.JSONField(default={"brus": 200}),
        ),
    ]
