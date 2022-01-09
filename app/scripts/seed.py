import os
import json
from django.conf import settings
from athletes.models import Weightclass, Athlete, Fighter

file_path1 = os.path.join(settings.BASE_DIR, 'scripts/static/ufc_rankings.json')
file_path2 = os.path.join(settings.BASE_DIR, 'scripts/static/ufc_athletes_all.json')

# TODO: load json file to a list of dict
# with open('static/ufc_data.json') as f:
with open(file_path1) as f:
    rankings_data = json.load(f)

with open(file_path2) as f2:
    all_athletes = json.load(f2)

# TODO: there will be 2 identical weight classes as "Pound-for-Pound Top Rank"
# We need to to update our data in 2 places
# first update the "Pound-for-Pound Top Rank" for men as: "Men's Pound-for-Pound Top Rank"
# second update the "Pound-for-Pound Top Rank" for women as: "Women's Pound-for-Pound Top Rank"

count = 0
for el in rankings_data:
    if el['weight_class'] == "Pound-for-Pound Top Rank":
        count += 1
        if count == 1:
            el['weight_class'] = "Men's Pound-for-Pound"
        if count == 2:
            el['weight_class'] = "Women's Pound-for-Pound"
    if count == 2:
        break


# TODO: initially insert all the data into the tables


def insert_rankings_data():
    for el in rankings_data:
        Weightclass.objects.create(weight_class=el['weight_class'])

    weightclasses = Weightclass.objects.all()
    weight_class_list = [(w.weight_class, w.id) for w in weightclasses]
    
    weight_class_rankings_athletes = 0
    for el in rankings_data:
        weight_class_id = list(filter(lambda x: x[0] == el['weight_class'], weight_class_list))[0][1]

        weight_class_obj = Weightclass.objects.only('id').get(id=weight_class_id)
        weight_class_rankings_athletes += 1
        for fighter in el['fighters']:
            Athlete.objects.create(
                athlete_name=fighter['athlete_name'],
                rank=fighter['rank'],
                image_src=fighter['img_src'],
                champion=fighter['champion'],
                record=fighter['record'],
                nickname=fighter['nickname'],
                weight_class=weight_class_obj
            )
        print(f"Weight classes added:  {weight_class_rankings_athletes}")


def insert_fighters_data():
     # TODO: ADD ALL FIGHTERS
    all_fighters_count = 0
    for fighter in all_athletes:
        Fighter.objects.create(
            athlete_name=fighter["athlete_name"],
            image_src=fighter["img_src"],
            record=fighter["record"],
            nickname=fighter["nickname"],
            weight_class=fighter["weight_class"]
        )
        all_fighters_count += 1
        if all_fighters_count % 12 == 0:
            print("Fighters added: ", all_fighters_count)
    
    print("Total fighters: ", all_fighters_count)
    


def run():
    # Optional
    Athlete.objects.all().delete()
    Weightclass.objects.all().delete()
    Fighter.objects.all().delete()

    insert_fighters_data()
    insert_rankings_data()
    print("************ Completed ************")
    

run()
