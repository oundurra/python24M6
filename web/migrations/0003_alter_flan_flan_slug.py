# Generated by Django 5.0.6 on 2024-07-18 01:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("web", "0002_flan"),
    ]

    operations = [
        migrations.AlterField(
            model_name="flan",
            name="flan_slug",
            field=models.SlugField(default=""),
        ),
    ]