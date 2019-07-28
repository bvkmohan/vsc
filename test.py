import requests

r = requests.get("http://www.bvkmohan.com")
print(r.status_code)
print(r.ok)
