import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as et

url = input("Enter location: ")

print("Retrieving", url)
xmlStr = urllib.request.urlopen(url).read()
print("Retrieved {} characters".format(len(xmlStr)))

xmlTree = et.fromstring(xmlStr)
counts = xmlTree.findall('.//count')

sum = 0

for count in counts:
    sum += int(count.text)

print(sum)