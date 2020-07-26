import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

#Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
count = input('count: ')
position = input('position: ')

# Requires +1 for inital url check
for value in range(0, int(count) +1):
    print('Retrieving: ', url)
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    #Retrieves all of the anchor tags
    tags = soup('a')
    url = tags[int(position) -1].get('href', None)
    