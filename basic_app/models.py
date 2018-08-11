from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class UserInfoModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True)

    github_link = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    # username = models.CharField()

    def __str__(self):
        return self.user.username


