from matplotlib.pyplot import xlabel, ylabel
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pdb
import requests

from bs4 import BeautifulSoup as bs

rating_src = "./data/title.ratings.tsv"
episode_src = "./data/title.episode.tsv"
show = "tt0052520"


def get_rating(source, episodes):
    # takes multiple episodes
    # returns df of episode ratings and votes
    with open(source) as dfile:
        df = pd.read_csv(dfile, sep='\t', encoding='utf8')
        df_episodes = df.loc[df['tconst'].isin(episodes)]
    return df_episodes

def get_episodes(source, show):
    # load title.episode.tsv
    # filter parentTconst (col 2) for show
    # return list of seasons and episodes
    with open(source) as dfile:
        df = pd.read_csv(dfile, sep='\t', encoding='utf8')
        df_show = df.loc[df['parentTconst'] == show]
        df_show = df_show.astype({'seasonNumber': 'int32', 'episodeNumber': 'int32'})
        df_show = df_show.sort_values(by=['seasonNumber', 'episodeNumber'])
    return df_show

def get_show_name(show_url):
    http_response = requests.get(show_url)
    soup_html = bs(http_response.text, "html.parser")
    try:
        show_title = soup_html.find("h1", {"data-testid":"hero-title-block__title"}).get_text()
        return str(show_title)
    except: # pylint: disable=W0702
        return 0

def gen_heatmap(ratings):
    # create dataframe with show ratings
    # make seasons as headers
    # make episodes as rows
    # plot color based on rating from 0 to 10 
    pass

epi = get_episodes(episode_src, show)
epi_list = epi['tconst'].tolist()
epi_rating = get_rating(rating_src, epi_list)
epi_merge = epi.merge(epi_rating, on='tconst', how='outer')
epi_drop = epi_merge#.dropna()
print(epi_drop)

show_name = get_show_name('https://www.imdb.com/title/'+show).replace(':','')
size = (epi_drop['seasonNumber'].max()//2+1, epi_drop['episodeNumber'].max()//2+1)
# pdb.set_trace()
epi_map = epi_drop.pivot('episodeNumber', 'seasonNumber', 'averageRating')
# pdb.set_trace()
# sns.set(rc={'figure.figsize':size})
map = sns.heatmap(epi_map, annot=True, linewidths=0.5)
# pdb.set_trace()
map.set(xlabel='Seasons', ylabel='Episodes', title=show_name)
# svm = sn.heatmap(df_cm, annot=True,cmap='coolwarm', linecolor='white', linewidths=1)
# plt.show()

figure = map.get_figure()    
figure.savefig('./heatmaps/'+show_name+'.png', dpi=300)