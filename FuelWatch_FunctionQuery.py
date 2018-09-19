import feedparser
from pprint import pprint
complete_feed = feedparser.parse('https://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS')

#print(complete_feed.entries)

fuelprice_list = []

for entry in complete_feed['entries']:
    fuel_dict = {}
#fuelprice_list = [fuel_dict[entry["address"]]]

    fuel_dict['address'] = entry["address"]
    fuel_dict['price'] = entry["price"]

    fuelprice_list.append(fuel_dict)



#pprint(fuelprice_list)
#-------------------------------------------------------------------------------
#All functions
def fuelbyproduct(productid):
    url = feedparser.parse('https://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product='+productid)
    return url
def fuelbyday(day):
    url = feedparser.parse('https://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Day='+day)
    return url
#-------------------------------------------------------------------------------

todaysPrice = fuelbyday('today')
tomorrowsPrice = fuelbyday('tomorrow')

#
