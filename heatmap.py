import os
import json
import re
import time
import requests
import pdb

import pandas as pd
from bs4 import BeautifulSoup as bs

class TvShow():
    def get_season_episode():
        pass

    def get_ep_title():
        pass

    def get_ep_rating():
        pass

    def get_ep_rating_count():
        pass

    def get_ep_airdate():
        pass

    def get_ep_description():
        pass


def get_seasons(show_url):
    http_response = requests.get(show_url)
    soup_html = bs(http_response.text, "html.parser")
    try:
        seasons = soup_html.find("select", {"class":"ipc-simple-select__input"}).get_text().split("See all")
        return list(seasons[0])
    except: # pylint: disable=W0702
        return 0

def get_seasons(show_url):
    http_response = requests.get(show_url)
    soup_html = bs(http_response.text, "html.parser")
    sums = []
    try:
        description = soup_html.find_all("div", {"class":"item_description"})
        for desc in description:
            sums.append(desc.value)
        return sums
    except:
        return -1


def get_episodes(season_url):
    http_response = requests.get(season_url)
    soup_html = bs(http_response.text, "html.parser")
    episodes = soup_html.find_all("div", {"class":"list_item"})

    season = {}    

    for episode in episodes:
        details = {}
        sea_pair = episode.find_next("div").get_text().strip()
        details["episode"] = episode.find_next("meta", {"itemprop":"episodeNumber"})['content']
        details["airdate"] = episode.find_next("div", {"class":"airdate"}).get_text().strip()
        details["title"] = episode.find_next("a", {"itemprop":"name"})["title"]
        details["rating"] = episode.find_next("span", {"class":"ipl-rating-star__rating"}).get_text().strip()
        details["ratecount"] = episode.find_next("span", {"class":"ipl-rating-star__total-votes"}).get_text().strip('()')
        details["description"] = episode.find_next("div", {"class":"item_description"}).get_text().strip()
        season[sea_pair] = details
    return season

base_url = "https://www.imdb.com/title/tt0903747/episodes?season="

for x in range(1,6):
    season_url = base_url + str(x)
    data = get_episodes(season_url)
    
    with open('C:\\Users\\phngu\\dev\\imdb\\sample.txt', 'a') as dfile:
        dfile.write(json.dumps(data))
        dfile.write('\n')



# def main():
#     dir_path = os.path.dirname(os.path.realpath(__file__))
#     file_path = os.path.join(dir_path, "title.episode.tsv")
    
#     df = pd.read_csv(file_path, sep='\t')
#     unique = df['parentTconst'].unique()
#     print(unique, len(unique), len(df['parentTconst']))

# # BASE_URL = "https://www.imdb.com/"
# # show_url = BASE_URL + "/title/" + ""
# # episode_url = show_url + "/episodes?season=" 
# # link = "https://www.imdb.com/title/tt2861424/episodes?season=1"
# # print(get_season(link))

# if __name__ == "__main__":
#     main()