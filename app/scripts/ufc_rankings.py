from bs4 import BeautifulSoup
import requests
import os
import json
from django.conf import settings

file_path = os.path.join(settings.BASE_DIR, 'scripts/static/ufc_athletes_all.json')
with open('static/ufc_athletes_all.json') as f:
    all_athletes = json.load(f)

""" Web scraping with Beautifulsoup to get the data and save as Json file """
url = 'https://www.ufc.com/rankings'
data = requests.get(url)
default_image_src = "https://www.ufc.com/themes/custom/ufc/assets/img/no-profile-image.png"

html = BeautifulSoup(data.text, 'html.parser')
content = html.select('.view-grouping')

ufc_data = []

def generate_rankings_data():
    for el in content:
        temp_dict = {'fighters': []}
        weight_class = el.select('.view-grouping-header')[0].get_text()
        temp_dict['weight_class'] = weight_class
        grouping_content = el.select('.view-grouping-content')[0]
        table = grouping_content.select('table')

        # Todo: champions
        table_caption = table[0].select('caption')

        try:
            champion = table_caption[0].select('a')[0].get_text()
            champion_a = table_caption[0].select('a')
            soup1 = BeautifulSoup(str(champion_a), 'html.parser')
            elem = soup1.find(href=True)
            champion_url = f"https://www.ufc.com/{elem['href']}"
            data2 = requests.get(champion_url)

            soup2 = BeautifulSoup(data2.text, 'html.parser')
            champ_nickname = None
            champ_record = soup2.select('.hero-profile__division-body')[0].get_text()

            champ_img = table_caption[0].select('img')[0]
            champ_img_src = champ_img['src']


            try:
                champ_nickname = soup2.select('.field-name-nickname')[0].get_text()
                champ_nickname = champ_nickname[1:-1]
            except:
                print('nickname not found, value=None')

            temp_dict['fighters'].append({'athlete_name': champion,
                                        'rank': 0,
                                        'img_src': champ_img_src,
                                        'champion': True,
                                        'record': champ_record,
                                        'nickname': champ_nickname})
        except:
            print('____No champion available, adding default values____')
            default_image_src = "https://www.ufc.com/themes/custom/ufc/assets/img/no-profile-image.png"
            temp_dict['fighters'].append({'athlete_name': 'None',
                                    'rank': 0,
                                    'img_src': default_image_src,
                                    'champion': True,
                                    'record': '0',
                                    'nickname': 'None'})
    

        # Todo:  fighters
        table_tr = table[0].select('tr')

        for tr in list(table_tr):
            fighter_rank_string = tr.select('td.views-field-weight-class-rank')[0].get_text()
            fighter_rank = [int(s) for s in fighter_rank_string.split() if s.isdigit()][0]
            fighter_name = tr.select('a')[0].get_text()
            fighter_link = tr.select('a')[0]['href']
            fighter_url = f"https://www.ufc.com/{fighter_link}"
            data3 = requests.get(fighter_url)
            soup3 = BeautifulSoup(data3.text, 'html.parser')
            fighter_nickname = None
            fighter_record = soup2.select('.hero-profile__division-body')[0].get_text()

            athlete_detail = \
                list(filter(lambda x: x['athlete_name'].lower() == fighter_name.lower(), all_athletes))


            if athlete_detail:
                print('--found-- ', athlete_detail[0]['athlete_name'])
                default_image_src = athlete_detail[0]['img_src']
            else:
                print("not found : default image is being applied")
                default_image_src = "https://www.ufc.com/themes/custom/ufc/assets/img/no-profile-image.png"
                

            try:
                fighter_nickname = soup3.select('.field-name-nickname')[0].get_text()
                fighter_nickname = fighter_nickname[1:-1]
            except:
                print('nickname not found, value=None')

            temp_dict['fighters'].append({'athlete_name': fighter_name,
                                        'rank': fighter_rank,
                                        'img_src': default_image_src,
                                        'champion': False,
                                        'record': fighter_record,
                                        'nickname': fighter_nickname})

        ufc_data.append(temp_dict)


generate_rankings_data();

# Todo: save the data to a json file for later imports
with open('./static/ufc_rankings.json', 'w') as f:
    json.dump(ufc_data, f, indent=4)

"""run: python ufc_rankings.py to generate a new updated file, and replace it to the static folder in the scripts 
directory """



#################################################################################




#### THIS CODE IS BELOW NOT NEEDED - JUST UPDATING THE RANKINS MANUALLY ####

# with open('static/ufc_rankings_raw.json') as f:
#     rankings_data = json.load(f)

# with open('static/weight_classes.json') as f:
#     weight_classes_data = json.load(f)



# def set_weight_id(weight_class, weights):
#     res = list(filter(lambda element: element['weight_class'] == weight_class, weights))
#     if len(res) > 0:
#         return res[0]['id']
#     return None


# def genData(athletes_dict, weights_dict):
#     res = []
#     figher_id = 1
#     for ranking in athletes_dict:
#         temp_weight_class = ranking['weight_class']
#         weight_class_id = set_weight_id(temp_weight_class, weights_dict)
#         fighers = ranking['fighters']
        
#         for figher in fighers:
#             figher['weight_class'] = weight_class_id
#             figher['id'] = figher_id
#             res.append(figher)
#             figher_id += 1
#     return res


# fighters_list = genData(rankings_data, weight_classes_data)


# # Todo: save the data to a json file for later imports
# with open('./static/ufc_rankings.json', 'w') as f:
#     json.dump(fighters_list, f, indent=4)
