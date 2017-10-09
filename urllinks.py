import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
count = int(input('Enter Count:'))
position = int(input('Enter Position:'))
names = list()
times = 0
while count > times:
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    tag = soup('a')
    name = tag[position-1].string
    names.append(name)
    url = tag[position-1]['href']
    times += 1

print(names[-1])

