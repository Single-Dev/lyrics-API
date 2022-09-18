from django import forms
from dataclasses import fields
from .models import *


class AddApiForm(forms.ModelForm):
    class Meta:
        model = Api
        fields = ['title', 'artist', "lyrics", "ps", "author"]