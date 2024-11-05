from django.db import models
from django.contrib.auth.models import User

class FashionItem(models.Model):
    item_id = models.IntegerField(default=0, unique=True)
    gender = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    item_type = models.CharField(max_length=100)
    description = models.TextField()
    photo_path = models.TextField()
    likes_count = models.IntegerField(default=0, editable=False)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username