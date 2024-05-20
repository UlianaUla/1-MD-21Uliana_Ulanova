def test(h):
    k = 0
    num_str = str(h)
    num_len = len(num_str)
    if num_len % 2 != 0:
        print("Номер билета должен содержать четное количество цифр")
        return
    len2 = num_len // 2
    first= num_str[:len2]
    second= num_str[len2:]
    
    sum_first = sum(map(int, first))
    sum_second = sum(map(int, second))
    
    if sum_first == sum_second:
        print("Ваш билет счастливый")
    else:
        print("Увы")

h = int(input("Введите номер билета: "))
test(h)

    
