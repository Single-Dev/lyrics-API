from django.shortcuts import render, redirect
from api.models import *
from django.db.models import Q
from django.views import generic
from api.form import *
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

def form_save(request):
    if request.method  == "POST":
        form = AddApiForm(request.POST)
        if form.is_valid():
            form.save()
        return  redirect('app:succses')
    else:
        form = AddApiForm()
    
    context = {
        "form":form
    }
    return render(request, "pages/add.html", context)

class SuccsesView(generic.TemplateView):
    template_name = "pages/succses.html"