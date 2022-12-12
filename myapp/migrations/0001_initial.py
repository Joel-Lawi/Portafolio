# Generated by Django 4.1.4 on 2022-12-09 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Project",
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
                ("title", models.CharField(max_length=200)),
                ("description", models.TextField()),
                ("foto", models.ImageField(null=True, upload_to="")),
                ("tag", models.CharField(max_length=100)),
                ("url_git", models.URLField(null=True)),
            ],
        ),
    ]
