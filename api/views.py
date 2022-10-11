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

# Lyrics API
@api_view(["GET"])
@permission_classes((permissions.AllowAny, ))
def LyricsApiView(request):
    lyrics = Lyrics.objects.all()
    serializer = LyricsAPI(lyrics, many=True)
    return Response(serializer.data)
# Lyrics Single API
@api_view(["GET"])
@permission_classes((permissions.AllowAny, ))
def LyricsSingleApiView(request, pk):
    lyrics = Lyrics.objects.get(id=pk)
    serializer = LyricsAPI(lyrics, many=False)
    return Response(serializer.data)

# Craete Lyrics API
@api_view(["POST"])
@permission_classes((permissions.AllowAny, ))
def AddLyricsAPI(request):
    serializer = LyricsAPI(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(["POST"])
@permission_classes((permissions.AllowAny, ))
def EditLyricsAPI(request, pk):
    lyrics = Lyrics.objects.get(id=pk)
    serializer = LyricsAPI(instance=lyrics,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(["DELETE"])
@permission_classes((permissions.AllowAny, ))
def DeleteLyricsAPI(request, pk):
    lyrics = Lyrics.objects.get(id=pk)
    lyrics.delete()
    return Response("o'chirdiz")

class LyricsSearch(generics.ListAPIView):
    queryset = Lyrics.objects.all()
    serializer_class = LyricsAPI
    filter_backends = [filters.SearchFilter]
    search_fields = ['artist', 'title']

lyricsSearch = LyricsSearch.as_view()

class SignUpView(generic.CreateView):
    template_name = 'registration/signup.html'
    form_class = SignUpForm

    def get_success_url(self):
        return reverse("login")

class SuccsesView(generic.TemplateView):
    template_name = "pages/succses.html"