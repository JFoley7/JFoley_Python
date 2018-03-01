
import requests

jim_foley_url = 'https://games.crossfit.com/competitions/api/v1/competitions/open/2018/leaderboards?division=1&region=&country=US&state=NJ&region_search_display=New+Jersey&athlete=711138&athlete_display=Jim+Foley&scaled=0&sort=0&occupation=0'

#Url Request
r = requests.get(jim_foley_url)

#saving json response a text file to local
with open('rank.txt', 'w') as fd:
    fd.write(r.text)

#taking all quotes out of text file and saving a second one
with open('rank.txt', 'r') as fe, open('rank2.txt', 'w') as new:
    for line in fe:
        new.write(line.replace('"', '').replace("'", ""))

#parsing txt file to just find my name
from itertools import islice

with open("rank2.txt") as f:
    for line in f:
        if "Jim Foley" in line:
            a=''.join(islice(f,47))

#parsing txt again to just display overall rank
for item in a.split("\n"):
    if "overallRank" in item:
        rank=item.strip()

#substring to just include number from line
b = rank[12:16]


print('Jim Foley Overall Rank:', b)

