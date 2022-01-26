from django.contrib.auth.models import User
from django.db import models


class HubSpotCredentials(models.Model):
    client_id = models.CharField(max_length=255)
    client_secret = models.CharField(max_length=500)
    redirect_url = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "HubSpot Credentials"


class HubSpotToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    refresh_token = models.CharField(max_length=500)
    access_token = models.CharField(max_length=500)
