import itchat
import math
from PIL import Image

def get_Image():

    friends = itchat.get_friends(update = True)

    num = 1

    for i in friends:

        im = itchat.get_head_img(userName=i["UserName"])

        fileIm = open("D:\\Camera Roll\\微信头像\\"+str(num)+".jpg","wb")

        fileIm.write(im)

        fileIm.close

        num+=1

        print("NickName:"+i["NickName"]+"    City:"+i["City"])

    return num-1

def pic_connect(size):

        num = get_Image()

        everynum = int(math.sqrt(num))+1

        im_size = size*everynum

        im = Image.new("RGB",(im_size,im_size),(255,255,255))

        count = 1

        while count<=num:

            try:

                headimg = Image.open("D:\\Camera Roll\\微信头像\\"+str(count)+".jpg")

            except OSError:

                pass

            headimg = headimg.resize((size,size),Image.ANTIALIAS)

            im.paste(headimg,(int(count/everynum)*size,(count%everynum)*size))

            count = count + 1

        im.save("D:\\Camera Roll\\微信头像\\result.jpg")





def main ():

    itchat.auto_login(hotReload=True)

    pic_connect(30)

    itchat.run()

    itchat.logout()


if __name__ =="__main__":

    main()