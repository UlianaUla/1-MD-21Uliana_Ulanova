from PIL import Image
cart=Image.open('../../../../1-мд-21/Уланова Ульяна/Лабораторные/birthday.jpg')
cartc=cart.crop((100,70,200,150))
cartc.save('birthdaycrop.jpg',quality=95)
