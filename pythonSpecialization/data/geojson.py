import urllib.request, urllib.parse, urllib.error
import json

serviceurl = 'http://py4e-data.dr-chuck.net/json?'

while True:
    key = 42
    address = input('Enter location: ')
    print(address)
    if len(address) < 1: break

    print('encoding Address')
    url = serviceurl + urllib.parse.urlencode({'address': address, 'key': key})

    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved {} characters'.format(len(data)))

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue
    
    print('Place id',js['results'][0]['place_id'])