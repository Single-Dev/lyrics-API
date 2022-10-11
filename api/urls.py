from django.urls import path
from .views import *

app_name = "app"

urlpatterns = [
    path('', home, name="home"),
    path("apis/", LyricsApiView, name="apis"),
    path("add-api/", AddLyricsAPI, name="add_lyrics_api"),
    path("update-api/<int:pk>/", EditLyricsAPI, name="edit_lyrics_api"),
    path("api/<int:pk>/", LyricsSingleApiView, name="sing_api"),
    path("delete-api/<int:pk>/", DeleteLyricsAPI, name="delete_lyrics_api"),
    path("search-api/", lyricsSearch, name="lyrics_search"),
    path('submit-succses/', SuccsesView.as_view(), name="succses"),
]   