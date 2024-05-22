import json
with open('jsonfile.json','r')as file:
    jfile=json.load(file)
    for i in jfile['products']:
        print(i['name\n','price\n','weight\n','available\n'])
