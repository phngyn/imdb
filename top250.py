import requests
from bs4 import BeautifulSoup as bs

def get_top250(show_url = 'https://www.imdb.com/chart/toptv/'):
    show_list = []
    http_response = requests.get(show_url)
    soup_html = bs(http_response.text, 'html.parser')
    try:
        shows = soup_html.find_all('td', {'class': 'titleColumn'})
        for link in shows:
            title = link.get_text().replace('\n','').strip()
            show_list.append(str(title) + '\t' + link.a['href']) 
        return show_list
    except: # pylint: disable=W0702
        return 0

with open('top250.txt', 'w') as wfile:
    shows = get_top250()
    for show in shows:
        wfile.write(str(show+'\n'))
