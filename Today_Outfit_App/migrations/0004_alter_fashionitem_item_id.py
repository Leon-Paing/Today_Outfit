# Generated by Django 4.2.13 on 2024-05-19 13:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Today_Outfit_App", "0003_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="fashionitem",
            name="item_id",
            field=models.IntegerField(max_length=100),
        ),
    ]