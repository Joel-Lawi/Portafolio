# Generated by Django 4.1.4 on 2022-12-10 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="description",
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name="project",
            name="foto",
            field=models.ImageField(blank=True, null=True, upload_to="myapp/images"),
        ),
        migrations.AlterField(
            model_name="project",
            name="url_git",
            field=models.URLField(blank=True, null=True),
        ),
    ]
