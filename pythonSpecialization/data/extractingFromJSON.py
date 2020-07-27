import urllib.request, urllib.error, urllib.parse
import json

url = input('Enter location: ')

print('Retrieving', url)
jsonData = urllib.request.urlopen(url).read()
print('Retrieved {} characters'.format(len(jsonData)))

jsonDict = json.loads(jsonData)

sum = 0
for comment in jsonDict['comments']:
    sum += int(comment['count'])

print('Sum:', sum)