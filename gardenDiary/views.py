from django.shortcuts import render, get_object_or_404
from gardenDiary.models import post

### Home #######################
def home(request):
    context = {
        "title": "Home"
    }
    return render(request, "home.html", context)

### Gardeners ##################
def gardeners(request):

    context = {
        "title": "Gardeners",
    }
    return render(request, "gardeners.html", context)


### Garden Diary ###############
def gardenDiary(request):
    objRS = post.objects.all()
    context = {
        "title": "Garden Diary: Feed",
        "posts": objRS,
    }
    return render(request, "gardenDiary.html", context)

def gardenDiary_create(request):

    context = {
        "title": "Garden Diary: addNew",
    }
    return render(request, "gardenDiary.html", context)

def gardenDiary_update(request):

    context = {
        "title": "Garden Diary: update",
    }
    return render(request, "gardenDiary.html", context)

def gardenDiary_detail(request,id=None):
    objRS = get_object_or_404(post, id=id)
    context = {
        "title": "Garden Diary: viewDetail",
        "post": objRS,
    }
    return render(request, "gardenDiary_detail.html", context)

def gardenDiary_delete(request):

    context = {
        "title": "Garden Diary: delete",
    }
    return render(request, "gardenDiary.html", context)
