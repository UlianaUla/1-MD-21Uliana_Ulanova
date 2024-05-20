otk={'Новый год':'new year.jpeg','День рождения':'birthday','8 марта':'mart.jpeg'}
a=input("Какой праздник вас интересует?")
if a in otk:
    open_otk=otk[a]
    try:
        from PIL import cart
        image=cart.open(open_otk)
        image.show()
          
    except FileNotFoundError:
        print("Такой открытки нет")
else:
    print("Такой открытки нет")
