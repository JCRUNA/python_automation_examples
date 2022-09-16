import requests

url='http://www.columbia.edu/~fdc/sample.html'
response=requests.get(url=url)

print(response.status_code)

print(response.text)