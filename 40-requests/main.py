import requests

response = requests.get('https://raw.githubusercontent.com/MkNiz/py-automation/master/readme.md')
print("Status Code:", response.status_code)
print("Length:", len(response.text))
print("Contents:")
print(response.text)