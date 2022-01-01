import os
import json
from django.conf import settings
from athletes.models import Weightclass, RankingsAthlete


file_path = os.path.join(settings.BASE_DIR, 'scripts/static/ufc_rankings.json')

# TODO: load json file to a list of dict
# with open('static/ufc_data.json') as f:
with open(file_path) as f:
    data = json.load(f)

# TODO: there will be 2 identical weight classes as "Pound-for-Pound Top Rank"
# We need to to update our data in 2 places
# first update the "Pound-for-Pound Top Rank" for men as: "Men's Pound-for-Pound Top Rank"
# second update the "Pound-for-Pound Top Rank" for women as: "Women's Pound-for-Pound Top Rank"

count = 0
for el in data:
    if el['weight_class'] == "Pound-for-Pound Top Rank":
        count += 1
        if count == 1:
            el['weight_class'] = "Men's Pound-for-Pound"
        if count == 2:
            el['weight_class'] = "Women's Pound-for-Pound"
    if count == 2:
        break


# TODO: initially insert all the data into the tables
def run():
    # Optional
    Weightclass.objects.all().delete()
    RankingsAthlete.objects.all().delete()

    for el in data:
        Weightclass.objects.create(weight_class=el['weight_class'])

    weightclasses = Weightclass.objects.all()
    weight_class_list = [(w.weight_class, w.id) for w in weightclasses]

    for el in data:
        weight_class_id = list(filter(lambda x: x[0] == el['weight_class'], weight_class_list))[0][1]

        weight_class_obj = Weightclass.objects.only('id').get(id=weight_class_id)
        
        for fighter in el['fighters']:
        
            RankingsAthlete.objects.create(
                athlete_name=fighter['athlete_name'],
                rank=fighter['rank'],
                image_src=fighter['img_src'],
                champion=fighter['champion'],
                record=fighter['record'],
                nickname=fighter['nickname'],
                weight_class=weight_class_obj
            )



run()
