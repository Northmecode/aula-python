import re
import urllib3
import json


http = urllib3.PoolManager()
r = http.request('GET', 'https://www.google.com')
print(json.r.data.decode('utf-8'))
