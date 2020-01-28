import requests
from bs4 import BeautifulSoup
import datetime

URL = 'https://www.advance-rp.ru/'
server = ['Red','Green','Blue']

result =  '=====================' \
          '\n\/ СЕРВЕРА ADVANCE \/\n' \
          '=====================\n'

def get_html(URL):
    r = requests.get(URL)
    return r

def get_content(html):
    global result
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div',class_ = 'statistic_table_content')

    for item in items:
        for i in range(len(server)):
            server_list = item.find_all('div', class_='gamers')[i]
            server_online = server_list.find('span').text
            result = result + '{0}: {1}/1000\n'.format(str.upper(server[i]),server_online)


def parse():
    global result
    html = get_html(URL)
    if html.status_code == 200:
        get_content(html.text)
        print(result)

    else:
        print('Error')

parse()