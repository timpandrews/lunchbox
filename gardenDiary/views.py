from django.http import HttpResponse
from django.shortcuts import render

def home(request):

    context = {
        "title": "Garden Diary",
    }
    return render(request, "home.html", context)
