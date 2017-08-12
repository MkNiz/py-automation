import requests, json

print("Making request...")
response = requests.get("http://pokeapi.co/api/v2/pokemon/metapod/")
response.raise_for_status()
print("Request successful\n\n")

meta_dic = json.loads(response.text)
print(meta_dic['name'])
print("Abilities:")
for ability in meta_dic['abilities']:
    print("\t" + ability['ability']['name'])

print("Base Stats:")
for stat in meta_dic['stats']:
    print("\t"+ stat['stat']['name'] + ": " + str(stat['base_stat']))
    