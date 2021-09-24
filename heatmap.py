import os
import json
import re
import time
import requests

# from pandas import DataFrame
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

# link = "https://www.imdb.com/title/tt2861424/episodes?season=1"
BASE_URL = "https://www.imdb.com/"
show_url = BASE_URL + "/title/" + ""
episode_url = show_url + "/episodes?season=" 

def get_seasons(show_url):
    http_response = requests.get(show_url)
    soup_html = bs(http_response.text, "html.parser")
    try:
        seasons = soup_html.find("select", {"class":"ipc-simple-select__input"}).get_text().split("See all")
        return list(seasons[0])
    except: # pylint: disable=W0702
        return 0

def get_episodes(show_url):
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


link = "https://www.imdb.com/title/tt2861424/episodes?season=1"
def get_season(season_url):
    http_response = requests.get(season_url)
    soup_html = bs(http_response.text, "html.parser")
    details = {}
    season = {}
    episodes = soup_html.find_all("div", {"class":"list_item"})
    for epi in episodes:
        pair = epi.find_next("div").get_text().strip()
        episode = epi.find_next("meta", {"itemprop":"episodeNumber"})['content']
        airdate = epi.find_next("div", {"class":"airdate"}).get_text().strip()
        title = epi.find_next("a", {"itemprop":"name"})["title"]
        rating = epi.find_next("span", {"class":"ipl-rating-star__rating"}).get_text().strip()
        ratecount = epi.find_next("span", {"class":"ipl-rating-star__total-votes"}).get_text().strip('()')
        description = epi.find_next("div", {"class":"item_description"}).get_text().strip()
        season[pair] = details
        
    
    return season.keys(), season.values()




print(get_season(link))






