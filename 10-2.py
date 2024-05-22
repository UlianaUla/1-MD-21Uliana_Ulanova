import json
prod={}
prod['name']=input("Введите название продукта: ")
prod['price']=input("Введите цену продукта: ")
prod['weight']=int(input("Введите вес продукта: "))
prod['available']=input("Этот продукт есть? ")
with open('jsonfile.json','r')as file:
    jfile=json.load(file)
    jfile['products'].append(prod)
    for i in jfile['products']:
        print(i['name\n','price\n','weight\n','available\n'])
