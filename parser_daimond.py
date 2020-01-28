import requests
from bs4 import BeautifulSoup
import datetime

URL = 'https://diamondrp.ru/'
server = ['emerald','trilliant', 'crystal','sapphire','amber','ruby']
now = datetime.datetime.now()
time = 'DATA: ' + now.strftime('%d-%m-%y') + '\n\nTIME: ' + now.strftime('%H:%M') + '\n\n'
result = time + '=====================' \
                '\n\/ СЕРВЕРА DAIMOND \/\n' \
                '=====================\n'

# print('TEST: ', server[0])
# print(len(server))

# now.year - Year | now.month - Month | now.day - Day | hour, second, minute

# print(datetime.date.today())
# print(now.strftime('%d-%m-%y %H:%M'))  Время + дата с форматированием

def get_html(URL):
    r = requests.get(URL)
    return r

def get_content(html):
    global result
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('ul',class_ = 'servers modaling')
    for i in range(len(server)):
        items = soup.find_all('small')[i].text
        result = result + '{0}: {1}\n'.format(str.upper(server[i]), items)

    # for item in items:
    #     for i in range(len(server)):
    #         server_list = item.find('li', class_=str(server[i]))  # selection list server
    #         server_online = server_list.find('small').text                 # selection online server
    #         result = result + '{0}: {1}\n'.format(str.upper(server[i]),server_online)


def parse():
    global result
    html = get_html(URL)
    if html.status_code == 200:
        get_content(html.text)
        print(result)

    else:
        print('Error')

parse()

