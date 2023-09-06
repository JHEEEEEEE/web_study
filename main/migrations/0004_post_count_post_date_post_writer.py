# Generated by Django 4.2 on 2023-09-06 03:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0003_rename_postname_post_title"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="count",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="post",
            name="date",
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name="post",
            name="writer",
            field=models.CharField(default="Anontmous", max_length=30),
        ),
    ]