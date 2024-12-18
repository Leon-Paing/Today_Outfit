# Generated by Django 4.2.13 on 2024-05-18 15:26

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("Today_Outfit_App", "0002_delete_user"),
    ]

    operations = [
        migrations.CreateModel(
            name="FashionItem",
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
                ("item_id", models.CharField(max_length=100)),
                ("gender", models.CharField(max_length=100)),
                ("category", models.CharField(max_length=100)),
                ("item_type", models.CharField(max_length=100)),
                ("description", models.TextField()),
                ("photo_path", models.TextField()),
                ("likes_count", models.IntegerField(default=0)),
            ],
        ),
    ]
