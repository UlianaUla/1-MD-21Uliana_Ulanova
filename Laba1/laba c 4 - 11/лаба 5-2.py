spisok=[1,1,2,3,4,4,5,6,7,8,3]
mnog=set()
mnog2=set()
for i in spisok:
    if i in mnog2:
        mnog.add(i)
    else:
        mnog2.add(i)
if mnog:
    print("Повторяющиеся элементы в списке ")
    for i in mnog:
        print(i)
else:
    print("В списке нет повторяющиихся элементов ")
    
