#!python3
from bs4 import BeautifulSoup
import requests
import re


link = 'https://teamcolorcodes.com/{}' + '-color-codes/'

colleges = ['ball-state-cardinals', 'duke-blue-devils']


def get_item(url):

    team_colors = [college]
    page = requests.get(url.format(college))
    soup = BeautifulSoup(page.text, 'html.parser')
    colors = soup.findAll("div", {"class": "colorblock"})
    hex = re.findall(r'#(?:[0-9a-fA-F]{6})', str(colors))
    set_hex = set(hex)
    team_colors.append(set_hex)
    return team_colors
            

if __name__ == '__main__':
    for college in colleges:
        print get_item(link)
