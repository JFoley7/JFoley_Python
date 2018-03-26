import requests

jim_foley_url = 'https://games.crossfit.com/competitions/api/v1/competitions/open/2018/leaderboards?division=1&region=&country=US&state=NJ&region_search_display=New+Jersey&athlete=711138&athlete_display=Jim+Foley&scaled=0&sort=0&occupation=0'

#Url Request
r = requests.get(jim_foley_url)
CF_data = (r.json())


for x in CF_data:
    print(x)

