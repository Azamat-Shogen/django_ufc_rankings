from django.db import models
from rest_framework import serializers
from athletes.models import RankingsAthlete, Weightclass


class WeightclassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weightclass
        fields = ('id', 'weight_class')


class RankingsAthleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = RankingsAthlete
        fields = ('id', 'athlete_name', 'rank', 
        'image_src', 'champion', 'record', 'nickname', 'weight_class')

