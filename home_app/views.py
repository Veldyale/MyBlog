from django.shortcuts import render
from .models import Home

def home(request):
    home = Home.objects
    return render(request, 'home_app/home.html', {'home': home})
