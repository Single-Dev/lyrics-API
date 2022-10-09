from rest_framework import serializers
from .models import Lyrics

class LyricsAPI(serializers.ModelSerializer):
    class Meta:
        model = Lyrics
        fields = "__all__"