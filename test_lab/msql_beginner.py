import urllib.parse
import requests
from mysql import connector

cn = connector.connect(user = 'franck christin', password = '199930Fr', host= 'localhost', database= 'msql' )
q = 'SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TAB'
c= cn.cursor()
c.execute(q)
for t in c :
    print (t)
cn.close()

main_api = 'http://maps.googleapis.com/maps/api/geocode/json?'
address = "lhr"
url = main_api + urllib.parse.urlencode({'address':address})
json_data = requests.get(url).json()

print(json_data)

