from operator import itemgetter

from django.shortcuts import render, redirect
from .models import *
import requests


def index(request):
    return render(request, 'index.html')


def auth(request):
    creds = HubSpotCredentials.objects.first()
    url = f"https://app.hubspot.com/oauth/authorize?client_id={creds.client_id}&" \
          f"redirect_uri={creds.redirect_url}&scope=oauth"
    return redirect(url)


def callback(request):
    code = request.GET['code']
    creds = HubSpotCredentials.objects.first()
    tokenResponse = requests.post("https://api.hubapi.com/oauth/v1/token",
                                  data={
                                      'grant_type': 'authorization_code',
                                      'client_id': creds.client_id,
                                      'client_secret': creds.client_secret,
                                      'redirect_uri': creds.redirect_url,
                                      'code': code
                                  })
    access_token = itemgetter('access_token')(tokenResponse.json())
    refresh_token = itemgetter('refresh_token')(tokenResponse.json())
    HubSpotToken.objects.create(user=request.user, access_token=access_token, refresh_token=refresh_token)

    data = {
        "access_token": access_token,
        "refresh_token": refresh_token
    }
    return render(request, "success.html", data)
