from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect, Http404
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

### Tools ##################
def tools(request):

    context = {
        "title": "Tools",
    }
    return render(request, "tools.html", context)


### Garden Diary ###############
def gardenDiary_list(request):
    obj = post.objects.all().order_by("-timestamp")
    paginator = Paginator(obj, 5) # Show n items per page

    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)

    context = {
        "title": "Garden Diary: Feed",
        "posts": posts,
    }

    return render(request, "gardenDiary_list.html", context)

def gardenDiary_create(request):
    if not request.user.is_authenticated:
        raise Http404

    form = postForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        messages.success(request, "Successfully Created")
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "title": "Garden Diary: addNew",
        "form": form,
    }
    return render(request, "gardenDiary_form.html", context)

def gardenDiary_update(request, id=None):
    if not request.user.is_authenticated:
        raise Http404

    obj = get_object_or_404(post, id=id)

    form = postForm(request.POST or None, request.FILES or None, instance=obj)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Successfully Updated")
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "title": "Garden Diary: update",
        "post": obj,
        "form": form
    }
    return render(request, "gardenDiary_form.html", context)

def gardenDiary_detail(request,id=None):
    obj = get_object_or_404(post, id=id)

    context = {
        "title": "Garden Diary: viewDetail",
        "post": obj,
    }
    return render(request, "gardenDiary_detail.html", context)

def gardenDiary_delete(request, id=None):
    if not request.user.is_authenticated:
        raise Http404

    obj = get_object_or_404(post, id=id)

    obj.delete()
    messages.success(request, "Success: Record Deleted")
    return redirect("gardenDiary:list")
