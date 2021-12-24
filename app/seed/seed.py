import os
import json
from athletes.models import Weightclass, Athlete


# TODO: load json file to a list of dict
with open('ufc_data.json') as f:
    data = json.load(f)


# TODO: initially insert all the data into the tables

def run():
    # Optional
    Weightclass.objects.all().delete()
    Athlete.objects.all().delete()

    for el in data:
        Weightclass.objects.create(weight_class=el['weight_class'])

