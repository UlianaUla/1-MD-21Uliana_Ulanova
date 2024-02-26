slovo=''
num=int(input())
for i in range(num):
    slovo2=input()
    if slovo2=='stop':
        break
    slovo+= slovo2+ ''
print(slovo)