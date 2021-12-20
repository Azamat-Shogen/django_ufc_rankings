from django.db import models

# Create your models here.
class Weightclass(models.Model):
    weight_class = models.CharField(max_length=200, blank=False, unique=True)


class Athlete(models.Model):
    athlete_name = models.CharField(max_length=200, blank=False)
    rank = models.IntegerField(blank=False, unique=True)
    image_src = models.CharField(max_length=200, default="#")
    champion = models.BooleanField(default=False)
    record = models.CharField(max_length=200, blank=False)
    nickname = models.CharField(max_length=200, default="")
    weight_class_id = models.ForeignKey(Weightclass, on_delete=models.CASCADE)