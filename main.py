import requests
import json

headers = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
}

input = input('>> ')

response = requests.get(
    'http://google.com/complete/search?client=chrome&q='+input, headers=headers)
for result in json.loads(response.text)[1]:
    print(result)
