from PIL import Image as i
im=i.open('Jung.jpg')
width, height = im.size
print(width,height)
print(im.format)
print(im.mode)