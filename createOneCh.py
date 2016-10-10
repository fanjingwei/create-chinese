#encoding: utf-8

from PIL import Image, ImageFont, ImageDraw
import os
import sys,getopt
import struct
import random

#text = u"赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜戚谢邹喻柏水窦章云苏潘葛奚范彭郎鲁韦昌马苗凤花方俞任袁柳酆鲍史唐费廉岑薛雷贺倪汤滕殷罗毕郝邬安常乐于时傅皮卞齐康伍余元卜顾孟平黄和穆萧尹"
text = u"赵钱孙李周吴郑王冯陈"
chNum = len(text)

styles = ["FZSTK.TTF", #方正舒体
"FZYTK.TTF", #方正姚体
"simfang.ttf", #仿宋
"simhei.ttf", #黑体
"STCAIYUN.TTF", #华文彩云
"STFANGSO.TTF", #华文仿宋
"STXINGKA.TTF", #华文行楷
"STHUPO.TTF", #华文琥珀
"STKAITI.TTF", #华文楷体
"STLITI.TTF", #华文隶书
"STSONG.TTF", #华文宋体
"STXIHEI.TTF", #华文细黑
"STXINWEI.TTF", #华文新魏
"STZHONGS.TTF", #华文中宋
"simkai.ttf", #楷体
"SIMLI.TTF", #隶书
"simsun.ttc", #宋体
"SIMYOU.TTF", #圆幼
]
styleNum = len(styles)

def getBackGroud(index):
	im = Image.open(str(index)+".jpg",'r')
	maxX,maxY = im.size
	xEnd = maxX-48
	yEnd = maxY-48
	xStart = random.randint(0,xEnd)
	yStart = random.randint(0,yEnd)
	return im.crop((xStart,yStart,xStart+48,yStart+48))

if __name__ =='__main__': 
    opts,args = getopt.getopt(sys.argv[1:],"hf:s:x:y:b:c:")

    for op,arg in opts:
        if "-h" == op:
            print("parameters：")
            print("-h:show help")
            print("-f:set font style,such as:FZSTK.TTF")
            print("-s:set size,such as:32")
            print("-x:set start pos x,such as:0")
            print("-y:set start pos y,such as:0")
            print("-b:set back ground,vaild num is:1~63")
            print("-c:set ch,vaild num is text len,now is:0~9")
            sys.exit(0)
        else:
            if "-f" == op:
                font = arg
            elif "-s" == op:
                size = int(arg)
            elif "-x" == op:
                xp = int(arg)
            elif "-y" == op:
                yp = int(arg)
            elif "-b" == op:
                bg = int(arg)
            elif "-c" == op:
            	ch = int(arg)

    try:
    	font
    except NameError:
    	font = styles[random.randint(0,styleNum-1)]

    try:
    	size
    except NameError:
    	size = random.randint(32,40)

    try:
    	xp
    except NameError:
    	xp = random.randint(0,48-size)

    try:
    	yp
    except NameError:
    	yp = random.randint(-size/4,48-size-size/4)

    try:
    	bg
    except NameError:
    	bg = random.randint(1,63)

    try:
    	ch
    except NameError:
    	ch = random.randint(0,chNum-1)

    im = Image.new("1", (48, 48), (255))
    imRGB = getBackGroud(bg)

    dr = ImageDraw.Draw(im)
    drRGB = ImageDraw.Draw(imRGB)

    chFont = ImageFont.truetype(os.path.join("fonts", font), size)

    dr.text((xp, yp), text[ch], font=chFont, fill="#000000")
    drRGB.text((xp, yp), text[ch], font=chFont, fill="#000000")

    im.save("picture.png")
    imRGB.save("pictureRGB.png")
