import xml.etree.ElementTree as ET

data1 = '''<person>
    <name>Chuck</name>
    <phone type="intl">
        +1 734 303 4456
    </phone>
    <email hide="yes" />
</person>'''

data2 = '''<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Brent</name>
        </user>
    </users>
</stuff>'''

tree = ET.fromstring(data1)
stuff = ET.fromstring(data2)

print("Printing data1")
print()
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))
print()
print()
print("Printing data2")
print()
lst = stuff.findall('users/user')
print('User Count:', len(lst))
print()
for item in lst:
    print('Name', item.find('name').text)
    print('Id', item.find('id').text)
    print('Attribute', item.get("x"))
    print()