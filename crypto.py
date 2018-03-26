import requests
print()
#LTC API URL
ltc_url = 'https://api.coinmarketcap.com/v1/ticker/litecoin/'
#Get API Price
ltc = requests.get(ltc_url)
# make response in json
ltc_data = (ltc.json())
#Personal LTC prices
ltc_purchase_prices = [31.95*1, 37.73*.5, 49.96*.25, 49.62*.25, 38*1, 53.79*.5, 85.59*.64557151, 84.51*5.7951171, 68.95, 47.08, 86.85*.1, 269.49*.5, 198.23*.5, 190.80*.5]
ltc_holdings = float(12.04)
ltc_og_price = float(92.325)

#Retreive only price in USD
for p in ltc_data:
    print("LTC Price:", p['price_usd'], "USD")
#retrieve current holdings in USD
for x in ltc_data:
    print("I Have","$",float(x['price_usd'])*ltc_holdings, "in LTC")
#retrieve current profit in USD
for y in ltc_data:
    print("LTC Current Sell All Profit:", "$",float(x['price_usd'])*ltc_holdings - (ltc_og_price * ltc_holdings))

    
#Ripple
ripple_url = 'https://api.coinmarketcap.com/v1/ticker/ripple/'
xrp = requests.get(ripple_url)
xrp_data = (xrp.json())

#personal ripple prices
xrp_og_price = float(1.32)
xrp_holdings = float(80.92)
print()
for p in xrp_data:
    print("Ripple Price:", p['price_usd'], "USD")
for x in xrp_data:
    print("I Have", "$",float(x['price_usd'])*xrp_holdings, "in Ripple")
for y in xrp_data:
    print("Ripple Current Sell All Profit:", "$", float(x['price_usd'])*xrp_holdings - (xrp_og_price * xrp_holdings))

#ETH
eth_url = 'https://api.coinmarketcap.com/v1/ticker/ethereum/'
eth = requests.get(eth_url)
eth_data = (eth.json())
eth_holdings = float(.00381197)
eth_og_price = float(403.45)
print()
for p in eth_data:
    print("ETH Price:", p['price_usd'], "USD")
for x in eth_data:
    print("I Have","$", float(x['price_usd'])*eth_holdings, "in ETH")
for y in eth_data:
    print("ETH Current Sell All Profit:", "$", float(x['price_usd'])*eth_holdings - (eth_og_price * eth_holdings))

#BTC
print()
btc_url = 'https://api.coinmarketcap.com/v1/ticker/bitcoin/'
btc = requests.get(btc_url)
btc_data = (btc.json())
for p in btc_data:
    print("BTC Price:", p['price_usd'], "USD")

print()
