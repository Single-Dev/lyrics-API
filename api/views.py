from django.shortcuts import render, redirect, reverse
from api.models import *
from django.db.models import Q
from django.views import generic
from api.form import *
from api.serializer import *
#rest_framework
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions, filters, generics


def home(request):
    return render(request, "pages/home.html")

@api_view(["GET"])
@permission_classes((permissions.AllowAny, ))
def LyricsApiView(request):
    lyrics = Lyrics.objects.all()
    serializer = LyricsAPI(lyrics, many=True)
    return Response(serializer.data)

class SignUpView(generic.CreateView):
    template_name = 'registration/signup.html'
    form_class = SignUpForm

    def get_success_url(self):
        return reverse("login")

class SuccsesView(generic.TemplateView):
    template_name = "pages/succses.html"