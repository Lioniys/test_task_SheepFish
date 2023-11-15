from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    personal_info = models.CharField(max_length=255)


class Site(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="sites")
    name = models.CharField(max_length=255)
    url = models.URLField()
    page_views = models.IntegerField(default=0)
    data_sent = models.FloatField(default=0)
    data_received = models.FloatField(default=0)
