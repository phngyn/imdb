import requests
from bs4 import BeautifulSoup as bs

url = "https://www.imdb.com/chart/toptv/"
def get_shows(show_url):
    show_list = []
    http_response = requests.get(show_url)
    soup_html = bs(http_response.text, "html.parser")
    try:
        shows = soup_html.find_all('td', {'class': 'titleColumn'})
        for link in shows:
            # print(link)
            show_list.append(link.a['href'])
        return show_list
    except: # pylint: disable=W0702
        return 0

shows = get_shows(url)

with open('top250.txt', 'a') as wfile:
    for show in shows:
        wfile.write(str(show+'\n'))
