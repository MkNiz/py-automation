import json

jstring = '{"id": 1, "name": "Goblin", "atk": 16, "def": 12, "alive": true}'

dic_from_json = json.loads(jstring)

for k, v in dic_from_json.items():
    print(k + ": " + str(v))
    