import os

import ImageFilter
from PIL import image
way1='D:\UserFolders\Desktop'
way2='D:\UserFolders\Desktop'
for i in os.listdir():
    a=image.open(i)
    b=image.filter(ImageFilter.BLUR)
    os.makedirt(way2)
    a.save('new_image.png')
    os.replace("")
    if image.endswith('.png'):
        for imagep in imagep:
            try:




