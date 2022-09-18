from django.shortcuts import render
from api.models import *
from django.db.models import Q
def home(request):
    return render(request, "pages/home.html")

def search_view(request):
    get = request.GET.get("search", "")
    if 'search' in request.GET:
        search = request.GET['search']
        full_search = Q(Q(artist__icontains=search) | Q(Q(title__icontains=search)))
        api = Api.objects.filter(full_search)[:1]
    else:
        api = Api.objects.all()
    context = {
        "api":api,
        "get":get
    }
    return render(request, "pages/results.html", context)