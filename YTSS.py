import requests
#from bs4 import BeautifulSoup

#textToSearch = 'at bat'
#query = requests.get(textToSearch)
#url = "https://www.youtube.com/results?search_query=" + query
#response = urllib2.urlopen(url)
#html = response.read()
#soup = BeautifulSoup(html)
#for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
#    print('https://www.youtube.com' + vid['href'])




search_url = 'https://www.youtube.com/results?search_query='

#Url Request
r = requests.get(search_url)

