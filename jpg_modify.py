# -*- coding: UTF-8 -*-
from PIL import Image,ImageFont, ImageDraw

import random


msgnum=str((random.randint(1,99)))

im = Image.open('/Users/nelsonpeng/123.png')

w,h =im.size

wdraw = 0.8*w

hdraw = 0.2*h

fron = ImageFont.truetype('Keyboard.ttf',200)

draw = ImageDraw.Draw(im)

draw.ellipse((wdraw,hdraw,wdraw+0.18*w,hdraw+0.18*h),fill="red")

draw.text((wdraw,hdraw),msgnum,font=fron,fill=(255,255,255))

im.save('/Users/nelsonpeng/test2.png','png')