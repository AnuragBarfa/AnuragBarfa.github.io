import requests
from requests.auth import HTTPBasicAuth
r=requests.get('https://www.linkedin.com/mynetwork/')
print(r.text)
