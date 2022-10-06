from django.shortcuts import render, redirect, reverse
from api.models import *
from django.db.models import Q
from django.views import generic
from api.form import *
def home(request):
    
    return render(request, "pages/home.html")



class SignUpView(generic.CreateView):
    template_name = 'registration/signup.html'
    form_class = SignUpForm

    def get_success_url(self):
        return reverse("login")

class SuccsesView(generic.TemplateView):
    template_name = "pages/succses.html"