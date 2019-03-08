#!python3
from bs4 import BeautifulSoup
import requests
import re


link = 'https://teamcolorcodes.com/{}' + '-color-codes/'

link2 = 'https://teamcolorcodes.com/{}' + '-colors/'

colleges1 = ['duke-blue-devils', 'kentucky-wildcats',
            'virginia-cavaliers', 'st-johns-red-storm', 'ole-miss-rebels', 
            'nc-state-wolfpack', 'oklahoma-sooners', 
            'virginia-commonwealth-rams', 'temple-owls', 
            'florida-state-seminoles', 'kansas-state-wildcats',
            'iowa-state-cyclones', 'auburn-tigers', 'alabama-crimson-tide',
            'ohio-state-buckeyes', 'maryland-terrapins', 'nevada-wolfpack',
            'texas-tech-red-raiders', 'lipscomb-university-bisons', 
            'yale-bulldogs', 'old-dominion-monarchs', 'buffalo-bulls', 
            'iowa-hawkeyes', 'virginia-tech-hokies', 'cincinnati-bearcats',
            'florida-gators', 'arizona-state', 'kansas-jayhawks', 
            'houston-cougars', 'montana-grizzlies', 'uc-irvine-anteaters',
            'washington-huskies', 'baylor-bears', 'syracuse-orange',
            'texas-christian-horned-frogs', 'texas-longhorns', 
            'michigan-wolverines', 'texas-state-bobcats', 
            'wright-state-raiders']

colleges2 = ['michigan-state-spartans', 'gonzaga', 
            'mississippi-state-university-bulldogs', 'wisconsin-badgers',
            'new-mexico-state-aggies', 'louisiana-state-lsu-tigers', 'minnesota-golden-gophers',
            'seton-hall-pirates', 'marquette', 'purdue-boilermakers', 
            'south-dakota-state-jackrabbits', 'villanova-wildcats',
            'north-carolina-tar-heels', 'loyola-marymount-lions']


def color_codes(url):

    team_colors = [college]
    page = requests.get(url.format(college))
    soup = BeautifulSoup(page.text, 'html.parser')
    colors = soup.findAll("div", {"class": "colorblock"})
    hex = re.findall(r'#(?:[0-9a-fA-F]{6})', str(colors))
    set_hex = set(hex)
    team_colors.append(set_hex)
    return team_colors
     

if __name__ == '__main__':
    for college in colleges1:
        print(color_codes(link))
    for college in colleges2:
        print(color_codes(link2))
    more_colors = open("team_colors.txt", 'r').readlines()
    for line in more_colors:
        print(line)
    
