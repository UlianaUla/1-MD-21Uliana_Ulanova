h = int(input("Введите число: "))

def test(n):
    if h % 3 == 0:
        return "Число делится на 3"
    else:
        return "Введённое число на 3 не делится"

print(test(h))

