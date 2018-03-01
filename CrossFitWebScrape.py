#import libraries
import requests
from bs4 import BeautifulSoup

#collect data
page = requests.get('https://games.crossfit.com/leaderboard/open/2018?division=1&region=&state=NJ&country=US&region_search_display=New+Jersey&athlete=711138&athlete_display=Jim+Foley&scaled=0&sort=0&occupation=0')

#BeautifulSoup Object creation
soup = BeautifulSoup(page.text, 'html.parser')

#Pull text from website
#athlete_name_list = soup.find(class_='main-nav-container')
#athlete_name_list = soup.find(class_='main-content loading')
#athlete_name_list = soup.find('cell-inner')
#athlete_name_list_items = athlete_name_list.__getattribute__('Jim')

#loop to print out all athlete names
#for athlete_name in athlete_name_list_items:
 #   print(athlete_name.prettify())'''

 
container_contents = soup.find(table_= 'desktop athletes')
print(container_contents)


