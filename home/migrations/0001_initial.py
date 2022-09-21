# Generated by Django 4.1.1 on 2022-09-07 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Ourstory",
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
                ("name", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=50)),
                ("phone", models.IntegerField()),
                ("address", models.TextField()),
                ("date", models.DateField()),
            ],
        ),
    ]
