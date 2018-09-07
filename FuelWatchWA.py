import feedparser
from pprint import pprint
f = feedparser.parse('https://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS')
t = f.entries
totalEntries = len(t)-1

FuelEntries =[]
i=0
for i in range(totalEntries):
    FuelEntries.append(f.entries[i])
#pprint(FuelEntries)
pprint(FuelEntries)
