# Generated by Django 4.2 on 2023-09-06 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0006_alter_post_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="writer",
            field=models.CharField(default="Anonymous", max_length=30),
        ),
    ]
