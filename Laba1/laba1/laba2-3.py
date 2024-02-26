num=int(input())
strok=''
for i in range(num):
    strok1=input("Введите слово: ")
    if 'ф' in strok1:
        print("Ого! Это редкое слово!")
    else:
        print("Эх, это не очень редкое слово...")
