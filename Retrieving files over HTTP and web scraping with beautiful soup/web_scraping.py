import requests
from bs4 import BeautifulSoup

page = requests.get("http://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168")
soup = BeautifulSoup(page.content, 'html.parser')
seven_day = soup.find(id="seven-day-forecast")
forecast_items = seven_day.find_all(class_="tombstone-container")
tonight = forecast_items[7]

period = tonight.find(class_="period-name").get_text()
short_desc = tonight.find(class_="short-desc").get_text()

period_tags = seven_day.select(".tombstone-container .period-name")
periods = [pt.get_text() for pt in period_tags]

short_descs = [sd.get_text() for sd in seven_day.select(".tombstone-container .short-desc")]
descs = [d["title"] for d in seven_day.select(".tombstone-container img")]

e = {}
# set e
for element in short_descs:
    e.setdefault(element, 0)
    # add element : 0

    e[element] += 1
    # add 1 to element

w1 = max([len(x) for x in e])
s1 = "Weather"
s2 = "# periods"
w2 = len(s2)

s = "_"
for a, b in [[s1, s2], [s * w1, s * w2]]:
    s = "{:{w1}s} {:5s}{:<{w2}s}".format(a, " ", b, w1=w1, w2=w2)
    print(s)

for a in sorted(e.keys()):
    b = e[a]
    s = "{:{w1}} {:5s}{:<d}".format(a, " ", b, w1=w1)
    print(s)
