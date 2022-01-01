from django.db import models


default_image_src = "https://www.ufc.com/themes/custom/ufc/assets/img/no-profile-image.png"

# Create your models here.
class Weightclass(models.Model):
    weight_class = models.CharField(max_length=200, blank=False, unique=True)


class RankingsAthlete(models.Model):
    athlete_name = models.CharField(max_length=200, blank=False)
    rank = models.IntegerField(blank=False, unique=False)
    image_src = models.CharField(max_length=240, default=default_image_src, null=True)
    champion = models.BooleanField(default=False)
    record = models.CharField(max_length=200, blank=False)
    nickname = models.CharField(max_length=200, default="", null=True)
    weight_class = models.ForeignKey(Weightclass, on_delete=models.CASCADE)


class Athlete(models.Model):
    athlete_name = models.CharField(max_length=200, blank=False)
    image_src = models.CharField(max_length=240, default=default_image_src, null=True)
    record = models.CharField(max_length=200, blank=False)
    nickname = models.CharField(max_length=200, default="", null=True)
    weight_class = models.CharField(max_length=200, default="", null=False)