# Generated by Django 4.2.13 on 2024-05-19 13:26

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("Today_Outfit_App", "0004_alter_fashionitem_item_id"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="fashionitem",
            name="item_id",
        ),
    ]
