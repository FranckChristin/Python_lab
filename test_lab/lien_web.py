import urllib.request
import urllib.parse
import re                   # module d'expression rationnel
import simplejson as json
from open_file import *

s = re.compile('.*youtube\.com.*',re.IGNORECASE)
e= re.compile('<b>|</b>')

p= open_file()
print(p)                                     #ouverture du code openfile
q = urllib.parse.urlencode({'q' : 'video2brain ubuntu'})                     #ouverture du lien

url = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&%s' % (q)
print(url)
search = urllib.request.urlopen(url)
json = json.loads(search.read())

for r in json ['responseData']['resulte']:                       #ouverture et iteration afin de filter les liens
    if s.match(r['url']):
        print(e.sub('', r['title']), r['url'])

