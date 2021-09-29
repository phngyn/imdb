import pandas as pd
import pdb

rating_src = "./data/title.ratings.tsv"
episode_src = "./data/title.episode.tsv"
show = "tt2861424"


def get_rating(source, episodes):
    # takes multiple episodes
    # returns df of episode ratings and votes
    with open(source) as dfile:
        df = pd.read_csv(dfile, sep="\t")
        df_episodes = df.loc[df['tconst'].isin(episodes)]
        df_episodes = df_episodes.astype({'tconst': 'str'})
    return df_episodes

def get_episodes(source, show):
    # load title.episode.tsv
    # filter parentTconst (col 2) for show
    # return list of seasons and episodes
    with open(source) as dfile:
        df = pd.read_csv(dfile, sep="\t")
        df_show = df.loc[df['parentTconst'] == show]
        df_show = df_show.astype({'tconst': 'str', 'parentTconst': 'str', 'seasonNumber': 'int32', 'episodeNumber': 'int32'})
        df_show = df_show.sort_values(by=['seasonNumber', 'episodeNumber'])
    return df_show

def gen_heatmap(ratings):
    # create dataframe with show ratings
    # make seasons as headers
    # make episodes as rows
    # plot color based on rating from 0 to 10 
    pass

epi = get_episodes(episode_src, show)
epi_list = epi['tconst'].tolist()
epi_rating = get_rating(rating_src, epi_list)

print(epi.dtypes, epi_rating.dtypes)

# for e in epi['tconst']:
    # print(e, '\n', epi)
    # pdb.set_trace()
    # print(e in epi_rating['tconst'])

# epi.merge(epi_rating, on='tconst', how='outer')
# print(epi)

pdb.set_trace()