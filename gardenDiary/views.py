from django.http import HttpResponse
from django.shortcuts import render

def home(request):

    context = {
        "title": "Home",
    }
    return render(request, "home.html", context)

def gardenDiary(request):

    context = {
        "title": "Garden Diary",
    }
    return render(request, "gardenDiary.html", context)
