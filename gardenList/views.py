from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render


from django.contrib.auth.models import User

### Gardeners ##################
def gardeners(request):

    obj = User.objects.all()
    paginator = Paginator(obj, 5) # Show n items per page

    page = request.GET.get('page')
    try:
        gardenersList = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        gardenersList = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        gardenersList = paginator.page(paginator.num_pages)

    context = {
        "title": "Gardeners",
        "gardenersList": gardenersList,
    }

    return render(request, "gardeners.html", context)
