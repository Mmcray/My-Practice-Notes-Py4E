from urllib.request import urlopen
from urllib.request import urljoin
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import ssl


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Take the required URL and open it. It returns as dType bites
url = 'http://py4e-data.dr-chuck.net/comments_1258254.xml'
xml_bites = urlopen(url, context=ctx).read()
# Decode the bites, returns a string in XML looking format
xml_data = xml_bites.decode()

# Take the string and convert it into XML tree
tree = ET.fromstring(xml_data)
# Make a list in the tree of all comments -> comment
lst = tree.findall('comments/comment')

num = 0
total = 0

#Loop through the list, grabbing all count values, converting to int and summing them
# use x.find('what your looking for').text for single variable ex. name, age
# use x.get('wylf') for statements/attri ex. help=yes
for item in lst:
    num = int(item.find('count').text)
    total += num

print(num)
print(total)
