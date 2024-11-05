from django.apps import AppConfig


class TodayOutfitAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "Today_Outfit_App"

def ready(self):
    import Today_Outfit_App.signals