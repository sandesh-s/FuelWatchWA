import feedparser
from pprint import pprint



#-----------------------------------------------------------------------------
#HTML Code Here
html_file = open('table.html','w')
html_file.write('<h1>Address</h1>')
#------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#All functions
def fuelbyproduct(productid):
    url = feedparser.parse('https://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product='+productid)
    return url
def fuelbyday(day):
    url = feedparser.parse('https://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Day='+day)
    return url

def fuelDataBuilder(item):
    item_list = []
    for entry in item['entries']:
        item_dict = {}
        item_dict['address'] = entry["address"]
        item_dict['price'] = entry["price"]
        item_list.append(item_dict)
    return item_list


def fuelSorting(items):
    return sorted(items, key = lambda sorteditems: sorteditems['price'])

# def fuelSorting2(items):
#     return sorted(items, key = lambda somefunction[])
#
# def some(items):
#     return items['price']
#-------------------------------------------------------------------------------

todaysPrice = fuelbyday('today')
tomorrowsPrice = fuelbyday('tomorrow')

todaysPriceNotSorted = fuelDataBuilder(todaysPrice)
tomorrowsPriceNotSorted = fuelDataBuilder(tomorrowsPrice)

combinedPricesNotSorted = todaysPriceNotSorted + tomorrowsPriceNotSorted

combinedPricesSorted = fuelSorting(combinedPricesNotSorted)

# pprint(todaysPriceNotSorted[1])



#Converting todays and tomorrows Price into a string
html_file.write('<table> </table>')
for items in todaysPriceNotSorted:
    string_Address=''
    string_Price=''
    string_Address = items['address']
    string_Price   = items['price']
    html_file.write('''
    <tbody>
        <tr>
            <td> {} </td>
            <td> {} </td>
        </tr>
    </tbody>

    '''.format(string_Address,string_Price))
