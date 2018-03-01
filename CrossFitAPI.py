import requests

jim_foley_url = 'https://games.crossfit.com/competitions/api/v1/competitions/open/2018/leaderboards?division=1&region=&country=US&state=NJ&region_search_display=New+Jersey&athlete=711138&athlete_display=Jim+Foley&scaled=0&sort=0&occupation=0'

#Url Request
r = requests.get(jim_foley_url)

with open('rank.txt', 'w') as fd:
    fd.write(r.text)

from itertools import islice

with open("rank.txt") as f:
    for line in f:
        if "Jim Foley" in line:
            print(''.join(islice(f,47)))

