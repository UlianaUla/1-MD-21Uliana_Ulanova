alpha={'А':1,'В':1,'Е':1,'И':1,'Н':1,'О':1,'Р':1,'С':1,'Т':1,'Д':2,'А':1,'К':2,'Л':2,'М':2,'П':2,'У':2,'Б':3,'Г':3,'Ё':3,'Ь':3,'Я':3,'Й':4,'Ы':4,'Ж':5,'З':5,'Ч':5,'Ш':8,'Э':8,'Ю':8,'Ф':10,'Щ':10,'Ъ':10}
slovo=input("Введите слово: ")
#xx=sum(alpha.get(alpha,0) for x in alpha )
# print(sum([k for i
# in slovo for k,v in alpha.items() if i in v]))
def suma(a):
    k=0
    for i in a.upper():
        if i in alpha:
            k+=alpha[i]
    return
slovo=input("Введите слово: ")
suma2=suma(slovo)
