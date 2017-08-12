import json

myDic = {
    'name': "Joe",
    'class': "Wizard",
    'stats': {
        'str': 6,
        'dex': 10,
        'int': 18,
        'con': 11
    },
    'inventory': ["Ceremonial Knife", "Rope", "Spellbook"]
} 

json_from_dic = json.dumps(myDic)
print(json_from_dic)