from django.http import HttpResponse
from django.shortcuts import render

def gardenDiary_home(request):

    context = {
        "title": "Garden Diary",
    }
    return render(request, "gardenDiary.html", context)
