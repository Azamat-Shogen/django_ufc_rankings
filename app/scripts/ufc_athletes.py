from bs4 import BeautifulSoup
import requests
import json

""" Web scraping with Beautifulsoup to get the data and save as Json file """
""" currently there are 109 pages """

num = 1
ufc_data = []

while True:
    url = f"https://www.ufc.com/athletes/all?gender=All&search=&page={num}"
    data = requests.get(url)
    html = BeautifulSoup(data.text, 'html.parser')
    page_content = html.select(".l-flex--4col-1to4")

    data2 = BeautifulSoup(str(page_content), 'html.parser')
    list_items = data2.select(".l-flex__item")

    for athlete in list_items:
        
        try:
            flip_card_front = athlete.select(".c-listing-athlete-flipcard__front")[0]
            fighter_name = flip_card_front.select(".c-listing-athlete__name")[0].get_text().strip()
            fighter_img = flip_card_front.select('img')[0]
            fighter_img_url = fighter_img['src']
            record = flip_card_front.select(".c-listing-athlete__record")[0].get_text()
            weight_class = flip_card_front.select(".c-listing-athlete__title")[0].select(".field__item")[0].getText()
            nickname = None
            try:
                nickname = flip_card_front.select(".c-listing-athlete__nickname")[0].select(".field__item")[0].get_text()
                nickname = nickname[1:-1]
            except:
                print("nickname_not__found value=None")

            ufc_data.append({
                "athlete_name": fighter_name,
                "img_src": fighter_img_url,
                "record": record,
                "nickname": nickname,
                "weight_class": weight_class,
            })

        except:
            print("__empty_list_found skipping")

        

    # todo: stop loop if no contents
    if not page_content:
        print("____done loop____")
        break

    num += 1


# TODO: this is not needed in production:
fighter_id = 1
for fighter in ufc_data:
    fighter['id'] = fighter_id
    fighter_id += 1


# Todo: save the data to a json file for later imports
with open('./static/ufc_athletes_all.json', 'w') as f:
    json.dump(ufc_data, f, indent=4)

"""run: python ufc_athletes.py to generate a new updated file, and replace it to the static folder in the scripts 
directory """


