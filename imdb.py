import pandas as pd

file = "./data/title.ratings.tsv"
episodes = "./data/title.episode.tsv"
show = "tt2861424"


def get_rating(episode):
    # takes multiple episodes
    # returns dictionary of season, episode: rating
    pass

def get_episodes(source, show):
    # load title.episode.tsv
    # filter parentTconst (col 2) for show
    # return list of seasons and episodes
    with open(source) as dfile:
        df = pd.read_csv(dfile, sep="\t")
        df_show = df.loc[df['parentTconst'] == show]
        df_show = df_show.astype({'seasonNumber': 'int32', 'episodeNumber': 'int32'})
        df_show = df_show.sort_values(by=['seasonNumber', 'episodeNumber'])
    return df_show

def gen_heatmap(ratings):
    # create dataframe with show ratings
    # make seasons as headers
    # make episodes as rows
    # plot color based on rating from 0 to 10 
    pass

print(get_episodes(episodes, show))