from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.


def welcome(request):
    return HttpResponse("Welcome to the meeting planner!")


def date(request):
    return HttpResponse(f"This page was served at {datetime.now()}")


def about(request):
    return HttpResponse("my name is mud")
