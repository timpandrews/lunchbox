from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

from gardenDiary.forms import postForm
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
def gardenDiary_list(request):
    objRS = post.objects.all()
    context = {
        "title": "Garden Diary: Feed",
        "posts": objRS,
    }
    return render(request, "gardenDiary_list.html", context)

def gardenDiary_create(request):
    form = postForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Successfully Created")
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "title": "Garden Diary: addNew",
        "form": form,
    }
    return render(request, "gardenDiary_form.html", context)

def gardenDiary_update(request, id=None):
    objRS = get_object_or_404(post, id=id)

    form = postForm(request.POST or None, instance=objRS)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        message.sucess(request, "Successfully Updated")
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "title": "Garden Diary: update",
        "post": objRS,
        "form": form
    }
    return render(request, "gardenDiary_form.html", context)

def gardenDiary_detail(request,id=None):
    objRS = get_object_or_404(post, id=id)
    context = {
        "title": "Garden Diary: viewDetail",
        "post": objRS,
    }
    return render(request, "gardenDiary_detail.html", context)

def gardenDiary_delete(request, id=None):

    objRS = get_object_or_404(post, id=id)
    objRS.delete()
    messages.success(request, "Success: Record Deleted")
    return redirect("gardenDiary:list")
