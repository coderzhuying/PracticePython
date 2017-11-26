from PIL import Image,ImageFont,ImageDraw

def add_num(in_file,num,out_file):

    im = Image.open(in_file)

    font = ImageFont.truetype("C:/windows/fonts/Arial.ttf",50)      #加载一个字体对象，并指定字体大小

    fill_color = "#ff0000"

    draw = ImageDraw.ImageDraw(im)          #创建可用于在给定图像中绘制的对象

    width,height = im.size

    draw.text((width-80,0),str(num),fill=fill_color,font=font)         #在给定的位置绘制字符串,左上角为(0,0)

    im.save(out_file)       #保存图片



add_num("D:\\Camera Roll\\yinxingshu.jpg",50,"D:\\Camera Roll\\result.jpg")




