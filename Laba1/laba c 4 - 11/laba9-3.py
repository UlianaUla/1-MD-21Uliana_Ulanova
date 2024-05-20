cost=0
with open('Лист продуктов.csv','r') as file:
    for line in file:
        data=line.strip().split(',')
        product=data[0]
        col=int(data[1])
        cost2=int(data[2])
        cost+=col*cost2
        
print(f"\nИтоговая сумма:{cost}руб")
