from django.urls import path
from .views import *

app_name = "app"

urlpatterns = [
    path('', home, name="home"),
    path("results/", search_view, name="search"),
    path("addapi/", form_save, name="add"),
    path('submit-succses/', SuccsesView.as_view(), name="succses"),
]   