# coding=utf-8
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import requests
from bs4 import BeautifulSoup

response = requests.get("http://www.metoffice.gov.uk/pub/data/weather/uk/climate/stationdata/heathrowdata.txt")
# get txt file

data = response.text

highs = []
lows = []
highs_f = []  # result
lows_f = []

data_rows = []

rainfall = []
rainfall_f = []  # final #result

years = []
years_f = []

yearHigh_temp = {}
yearLows = {}
yearRainfall = {}

for row in data.split("\n")[7:]:
    # start row from 8th(7index) new lines

    fields = [x for x in row.split(" ") if x]
    # x is nothing, split(empty), if x is nothing
    # assign row[index]

    data_rows.append(fields)
    # append each row

    year = int(fields[0])  # first element of fields
    years.append(year)

    yearHigh_temp.setdefault(year, [])
    yearLows.setdefault(year, [])
    yearRainfall.setdefault(year, [])

    yearRainfall[year].append(float(fields[5]))  # For assigned year, 6th element of fields is added
    yearHigh_temp[year].append(float(fields[2]))  # For assigned year, 3rd element of fields is added
    yearLows[year].append(float(fields[3]))

    rainfall.append(float(fields[5]))
    highs.append(float(fields[2]))
    lows.append(float(fields[3]))

years_f = list(dict.fromkeys(yearHigh_temp))
## Dictionary An iterable specifying the keys of the new dictionary

lowest = 100
highest = 0

# get the highs and lows for the whole table( put in highs and lows )
for i in highs:
    if highest < i:
        highest = i

for i in lows:
    if lowest > i:
        lowest = i

# Double loop
for i in yearHigh_temp:
    l = len(yearHigh_temp[i])
    # length of the temperature list for this year

    high = 0

    for j in range(l):
        if (yearHigh_temp[i][j] > high):
            high = yearHigh_temp[i][j]
            # highest temperature for this year

    highs_f.append(high)

for i in yearLows:
    l = len(yearLows[i])
    low = 100
    # length of the temperature list for this year

    for j in range(l):
        if (yearLows[i][j] < low):
            low = yearLows[i][j]
            # lowest temperature for this year

    lows_f.append(low)

for i in yearRainfall:
    l = len(yearRainfall[i])
    # length of rainfall list for this year

    rain = 0

    for j in range(l):
        rain += yearRainfall[i][j]

    rainfall_f.append(rain / l)
    # avg rain fall

print("Average rainfall = {:.1f} mm".format(sum(rainfall) / len(rainfall)))
print("The highest temperature in degrees = {}".format(highest))
print("The lowest temperature in degrees = {}".format(lowest))
print("Year Highest_Degree  Lowest_Degree    Rainfall")

for i in range(len(years_f)):
    print("{0}{1:10}{2:15}{3:15.1f}".format(years_f[i], highs_f[i], lows_f[i], rainfall_f[i]))
    """{years_f[i]} {highs_f[i]: the number for the field size} {lows_f[i]: the number for the field size} 
        {rainfall_f[i]: the number for the field size. 1 decimal digit }"""
