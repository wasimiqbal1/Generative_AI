import requests

r = requests.post("http://localhost:8000/hi", json={"who": "Mom"})
print(r.json())
print(r.status_code)
print(r.headers)
print(r.text)