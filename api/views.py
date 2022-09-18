from django.shortcuts import render
from api.models import *

def home(request):
    return render(request, "pages/home.html")

def search_view(request):
    get = request.GET.get("search", "")
    if get and get != "":
        api = Api.objects.filter(title__contains=get).all()
    else:
        api = ''
    context = {
        "api":api,
        "get":get
    }
    return render(request, "pages/search.html", context)