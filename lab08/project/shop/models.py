from django.db import models


class Anime(models.Model):
    name = models.CharField(max_length=20)


class Description(models.Model):
    anime_id = models.ForeignKey(Anime, on_delete=models.CASCADE)
    description = models.CharField(max_length=600)