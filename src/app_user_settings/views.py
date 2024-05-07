from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def user_settings(request):
    return HttpResponse('''Hello World, You're on user settings page''')
