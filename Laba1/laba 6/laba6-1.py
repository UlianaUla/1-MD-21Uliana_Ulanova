slovar={'Россия': Москва,'Германия': Берлин,'Польша': Варшава,'Чехия': Прага,'Сербия': Белград,'Япония': Токио,}

for st, stl in slovar.items():
    print(st,stl)
x=input("Введите страну: ")
#print(f'{x}:{slovar.get(x)}')

#sorted_slovar=sorted(slovar.items(),key=lambda item: item[1])
s=sorted(slovar.keys())
print()
for x in s:
    print(f'{x}:{slovar [x]}')