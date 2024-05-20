def test():
    day=int(input("Введите день"))
    month=int(input("Введите месяц"))
    year=int(input("Введите год"))
    res=day*month
    res2=year % 100
    if res==res2:
        return True
    else:
        return False
print(test())
