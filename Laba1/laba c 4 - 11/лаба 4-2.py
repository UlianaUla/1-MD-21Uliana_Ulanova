try:
    h=int(input("Введите число"))
    res=100/h
    print("Результат",res)
except ValueError:
    print("Пожалуйста,вводите только числа")
except ZeroDivisionError:
    print("На ноль делить нельзя")
    
