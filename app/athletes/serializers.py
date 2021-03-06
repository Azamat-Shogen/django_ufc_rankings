from django.db import models
from rest_framework import serializers
from athletes.models import Athlete, Weightclass, Fighter


class WeightclassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weightclass
        fields = ('id', 'weight_class')


class AthleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Athlete
        fields = ('id', 'athlete_name', 'rank', 
        'image_src', 'champion', 'record', 'nickname', 'weight_class')


class FighterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fighter
        fields = ('id', 'athlete_name', 
        'image_src', 'record', 'nickname', 'weight_class')