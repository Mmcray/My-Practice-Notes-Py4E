import json
from urllib.request import urlopen
import ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_1258255.json'
jsu = urlopen(url, context=ctx).read()
js_data = jsu.decode()
jsl = json.loads(js_data)
lst = []
sm = 0
fnd = jsl.get('comments')
for names in fnd:
    lst.append(names.get(('count')))
for val in lst:
    sm += val
print(sm)

