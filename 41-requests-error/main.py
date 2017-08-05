import requests

response = requests.get('https://raw.githubusercontent.com/MkNiz/py-automation/master/doesnt_exist.txt')
ok = True
try:
    response.raise_for_status()
except Exception as ex:
    print("ERROR: {0}".format(ex))
    ok = False

if ok:
    print("Status Code:", response.status_code)
    print("Length:", len(response.text))
    print("Contents:")
    print(response.text)
else:
    print("Response was not OK.")