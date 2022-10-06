from django.urls import path
from .views import *

app_name = "app"

urlpatterns = [
    path('', home, name="home"),
    path('submit-succses/', SuccsesView.as_view(), name="succses"),
]   