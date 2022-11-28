import json

with open("data.json") as file:
    data = json.load(file)



for d in data:
    for key, value in d.items():
        print(key," : ",value)

    