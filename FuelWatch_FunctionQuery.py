import feedparser
from pprint import pprint

#-------------------------------------------------------------------------------
#All functions
#this function return fuel prices by fuel type ULP, premium fuel
def fuelbyproduct(productid):
    url = feedparser.parse('https://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product='+productid)
    return url
#this function returns fuel prices by day i.e. today or tomorrow
def fuelbyday(day):
    url = feedparser.parse('https://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Day='+day)
    return url

#this function structures the data by building list of dictionaries
def fuelDataBuilder(item):
    item_list = []
    for entry in item['entries']:
        item_dict = {}
        item_dict['address'] = entry["address"]
        item_dict['price'] = entry["price"]
        item_list.append(item_dict)
    return item_list

#this function sorts the list by fuel prices
def fuelSorting(items):
    return sorted(items, key = lambda sorteditems: sorteditems['price'])
#-------------------------------------------------------------------------------

todaysPrice = fuelbyday('today')
tomorrowsPrice = fuelbyday('tomorrow')

todaysPriceNotSorted = fuelDataBuilder(todaysPrice)
tomorrowsPriceNotSorted = fuelDataBuilder(tomorrowsPrice)

combinedPricesNotSorted = todaysPriceNotSorted + tomorrowsPriceNotSorted

combinedPricesSorted = fuelSorting(combinedPricesNotSorted)

pprint(combinedPricesSorted)


#
