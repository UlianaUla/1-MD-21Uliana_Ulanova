from PIL import Image
image= Image.open('Jung.jpg')
reduce_image=image.reduce(3)
rotate_img=image.rotate(180)
rotate2_img=image.rotate(90)
reduce_image.save('Red.png')
rotate_img.save('Yellow.png')
rotate2_img.save('Green.png')
