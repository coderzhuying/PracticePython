from PIL import Image,ImageDraw,ImageFont,ImageFilter
import random

def makeyzm(count):

    im = Image.open("D:\\Camera Roll\\来者何人.jpg").filter(ImageFilter.BLUR).resize((240,80))



    font = ImageFont.truetype("C:/windows/fonts/Arial.ttf",50)

    fill_color = "#ff6060"

    draw = ImageDraw.ImageDraw(im)

    for i in range(1,5):

        num = random.randint(0, 20)

        height = random.randint(0,30)

        if num < 10:

            str1 = str(num)

        else:

            str1 = chr(random.randint(65,90))

        draw.text((i*50,height),str1,fill=fill_color,font=font)

    im2 = im.filter(ImageFilter.BLUR)

    im2.save("D:\\Camera Roll\\yanzhengma"+str(count)+".jpg")

for i in range(1,10):

    makeyzm(i)