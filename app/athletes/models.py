from django.db import models


default_image_src = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTdxD4o2sWDv53TYcVsOpMoRLuzZn1-1pA7iA&usqp=CAU"

# Create your models here.
class Weightclass(models.Model):
    weight_class = models.CharField(max_length=200, blank=False, unique=True)


class Athlete(models.Model):
    athlete_name = models.CharField(max_length=200, blank=False)
    rank = models.IntegerField(blank=False, unique=False)
    image_src = models.CharField(max_length=200, default=default_image_src, null=True)
    champion = models.BooleanField(default=False)
    record = models.CharField(max_length=200, blank=False)
    nickname = models.CharField(max_length=200, default="", null=True)
    weight_class = models.ForeignKey(Weightclass, on_delete=models.CASCADE)

    