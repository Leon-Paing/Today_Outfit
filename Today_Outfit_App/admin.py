from django.contrib import admin
from .models import FashionItem
from .models import UserProfile

class FashionItemAdmin(admin.ModelAdmin):
    readonly_fields = ('likes_count',)

    list_display = ('item_id', 'gender', 'category', 'item_type', 'description', 'photo_path','likes_count',)

admin.site.register(FashionItem, FashionItemAdmin)
admin.site.register(UserProfile)