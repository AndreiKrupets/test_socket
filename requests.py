import requests
url = 'tut.by'
r = requests.get(url)
print('Status code:', r.status.code)
responce_dict = r.json()
print((responce_dict.keys()))