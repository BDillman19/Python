import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter - ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

sum = 0
#Retrieves all of the anchor tags
tags = soup('span')
for tag in tags:
    sum += int(tag.contents[0])

print(sum)