import requests
#LTC API URL
ltc_url = 'https://api.coinmarketcap.com/v1/ticker/litecoin/'
#Get API Price
ltc = requests.get(ltc_url)
# make response in json
ltc_data = (ltc.json())
#Retreive only price in USD
for p in ltc_data:
    print("LTC:", p['price_usd'],)
