# -*- coding:utf-8 -*-

from PIL import Image
# import argparse
#
# #命令行参数处理
# parser=argparse.ArgumentParser()
#
# parser.add_argument('file')#输入文件
# parser.add_argument('-o','--output')#输出文件
# parser.add_argument('--width',type=int,default=80)
# parser.add_argument('--height',type=int,default=80)

# 获取参数
# args=parser.parse_args()

IMG='/Users/nelsonpeng/Downloads/cx.jpg'
# WIDTH=args.width
# HEIGHT=args.height
# OUTPUT=args.output'
WIDTH=100
HEIGHT=100

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

# 将256灰度映射到70个字符上

def get_char(r, g, b, alpha=256):
    # alpha透明度
    if alpha==0:
        return ' '
    length = len(ascii_char)
    gray = int(0.2126*r+0.7152*g+0.0722*b)
    # 计算灰度
    unit=(256.0+1)/length
    return ascii_char[int(gray/unit)]
    # 不同的灰度对应着不同的字符
    # 通过灰度来区分色块

if __name__=='__main__':
    im=Image.open(IMG)
    im=im.resize((WIDTH,HEIGHT),Image.NEAREST)
    txt=""
    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += get_char(*im.getpixel((j,i)))
            if j%3==0:
                txt += get_char(*im.getpixel((j, i)))


        txt+='\n'

    print(txt)

    # 字符画输出到文件
    # if OUTPUT:
    #     with open(OUTPUT,'w') as f:
    #         f.write(txt)
    # else:
    #     with open("output.txt",'w') as f:
    #         f.write(txt)

    with open("/Users/nelsonpeng/Downloads/output.txt",'w') as f:
        f.write(txt)