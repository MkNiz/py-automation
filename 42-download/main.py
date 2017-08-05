import requests

response = requests.get('https://raw.githubusercontent.com/MkNiz/py-automation/master/readme.md')
print("Status Code:", response.status_code)
response.raise_for_status()

print("Length:", len(response.text))
print("Contents:")
print(response.text)

print("\nCopying file to current working directory...")

localFile = open('downloaded_file.md', 'wb')

for chunk in response.iter_content(100000):
    localFile.write(chunk)
    
localFile.close()

print("Finished")

