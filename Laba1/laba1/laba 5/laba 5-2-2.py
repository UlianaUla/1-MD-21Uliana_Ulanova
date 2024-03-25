corteg=[1,2,3,4,1,2,6,7,8,9,3,5]
c={}# повторяющиеся элементы
for i in corteg:
    if i in c:
        print(i)
    else:
        c[i]=1
print(c)
