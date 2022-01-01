from bs4 import BeautifulSoup
import requests
import os
import json
from django.conf import settings

# file_path = os.path.join(settings.BASE_DIR, 'scripts/static/ufc_athletes_all.json')
with open('static/ufc_athletes_all.json') as f:
    all_athletes = json.load(f)

""" Web scraping with Beautifulsoup to get the data and save as Json file """
url = 'https://www.ufc.com/rankings'
data = requests.get(url)
default_image_src = "https://www.ufc.com/themes/custom/ufc/assets/img/no-profile-image.png"

html = BeautifulSoup(data.text, 'html.parser')
content = html.select('.view-grouping')

ufc_data = []

for el in content[:-1]:
    temp_dict = {'fighters': []}
    weight_class = el.select('.view-grouping-header')[0].get_text()
    temp_dict['weight_class'] = weight_class
    grouping_content = el.select('.view-grouping-content')[0]
    table = grouping_content.select('table')

    # Todo: champions
    table_caption = table[0].select('caption')
    champion = table_caption[0].select('a')[0].get_text()
    champion_a = table_caption[0].select('a')
    soup1 = BeautifulSoup(str(champion_a), 'html.parser')
    elem = soup1.find(href=True)
    champion_url = f"https://www.ufc.com/{elem['href']}"
    data2 = requests.get(champion_url)

    soup2 = BeautifulSoup(data2.text, 'html.parser')
    champ_nickname = None
    champ_record = soup2.select('.tz-change-inner')[0].get_text()
    champ_record = champ_record[champ_record.index("•") + 1:].strip()
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
        fighter_record = soup3.select('.tz-change-inner')[0].get_text()
        fighter_record = fighter_record[fighter_record.index("•") + 1:].strip()

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

# Todo: save the data to a json file for later imports
with open('./static/ufc_rankings.json', 'w') as f:
    json.dump(ufc_data, f, indent=4)

"""run: python ufc_rankings.py to generate a new updated file, and replace it to the static folder in the scripts 
directory """
