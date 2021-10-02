from matplotlib.pyplot import xlabel, ylabel
import pandas as pd
import numpy as np
from pandas.core.frame import DataFrame
import seaborn as sns
import matplotlib.pyplot as plt
import pdb
import requests

from bs4 import BeautifulSoup as bs

def get_ratings(episode_ids: pd.DataFrame) -> pd.DataFrame:
    # takes multiple episodes
    # returns df of episode ratings and votes
    data_source = "./data/title.ratings.tsv"
    episode_list = episode_ids['tconst'].tolist()
    with open(data_source) as dfile:
        df = pd.read_csv(dfile, sep='\t', encoding='utf8')
        df_episodes = df.loc[df['tconst'].isin(episode_list)]
    return df_episodes

def get_episodes(show_id: str) -> pd.DataFrame:
    # load title.episode.tsv
    # filter parentTconst (col 2) for show
    # return list of seasons and episodes
    data_source = "./data/title.episode.tsv"
    with open(data_source) as dfile:
        df = pd.read_csv(dfile, sep='\t', encoding='utf8')
        df_show = df.loc[df['parentTconst'] == show_id]
        df_show = df_show.astype({'seasonNumber': 'int32', 'episodeNumber': 'int32'})
        df_show = df_show.sort_values(by=['seasonNumber', 'episodeNumber'])
    return df_show

def get_show_name(show_id: str) -> str:
    show_url = 'https://www.imdb.com/title/'+show_id
    http_response = requests.get(show_url)
    soup_html = bs(http_response.text, "html.parser")
    try:
        show_title = soup_html.find("h1", {"data-testid":"hero-title-block__title"}).get_text().replace(':','')
        return str(show_title)
    except: # pylint: disable=W0702
        return 0

def gen_rating_map():
    pass

# def gen_heatmap(rating_map: pd.DataFrame):
#     # create dataframe with show ratings
#     # make seasons as headers
#     # make episodes as rows
#     # plot color based on rating from 0 to 10
#     df_mapped = rating_map.pivot('episodeNumber', 'seasonNumber', 'averageRating')

#     # sns.set(rc={'figure.figsize':size})
#     map = sns.heatmap(df_mapped, annot=True, linewidths=0.5, square=True, vmin=0, vmax=10)
#     # plt.show()

#     return map

def main():
    show_id = "tt0121955"

    show_name = get_show_name(show_id)
    episodes = get_episodes(show_id)
    episode_ratings = get_ratings(episodes)
    df_merged = episodes.merge(episode_ratings, on='tconst', how='outer')
    # df_merged_dropna = df_merged.dropna()
    # print(df_merged_dropna)

    # size = (df_merged['seasonNumber'].max()//2+1, df_merged['episodeNumber'].max()//2+1)

    df_mapped = df_merged.pivot('episodeNumber', 'seasonNumber', 'averageRating')

    # sns.set(rc={'figure.figsize':size})
    map = sns.heatmap(df_mapped, annot=True, linewidths=0.5, square=True, vmin=0, vmax=10)
    map.set(xlabel='Seasons', ylabel='Episodes', title=show_name)
    plt.show()
    
    figure = map.get_figure()
    # figure = gen_heatmap(df_merged)
    # figure.set(xlabel='Seasons', ylabel='Episodes', title=show_name)
    
    figure.savefig('./heatmaps/' + show_name+ ' - ' + show_id + '.png', dpi=300, pad_inches='0.2')

    return 0

if __name__ == "__main__":
    main()
