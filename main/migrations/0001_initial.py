# Generated by Django 4.2 on 2023-09-05 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("postname", models.CharField(max_length=50)),
                ("contents", models.TextField()),
            ],
        ),
    ]
