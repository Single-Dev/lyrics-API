from django.db import models
from django.contrib.auth.models import AbstractUser

class MyUser(AbstractUser):
    is_organiser = models.BooleanField(default=False)
    is_agent = models.BooleanField(default=False)


class Api(models.Model):
    title = models.CharField(max_length=30)
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    artist = models.CharField(max_length=200)
    lyrics = models.TextField(max_length=70000)
    ps = models.CharField(max_length=50, default="mrsenior.t.me")
    public = models.BooleanField(default=True)
    def __str__(self):
        return str(f"artis - {self.artist}, status: {self.public}")
