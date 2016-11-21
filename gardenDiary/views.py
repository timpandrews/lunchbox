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

def gardeners(request):

    context = {
        "title": "Gardeners",
    }
    return render(request, "gardeners.html", context)
