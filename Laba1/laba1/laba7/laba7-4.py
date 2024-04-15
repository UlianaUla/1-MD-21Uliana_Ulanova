from PIL import Image, ImageDraw, ImageFont
im=Image.open('1.jpg')
width,height = im.size
d=ImageDraw.Draw(im)
t="I want to be just like you"
f=ImageFont.truetype('arial.ttf',50)
twidth, theight=d.t(t,f)
m=10
x=width-twidth-m
y=height-theight-m
d.t((x,y),t,f=f)
im.show
im.save
