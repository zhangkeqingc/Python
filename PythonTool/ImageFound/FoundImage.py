

from PIL import Image
import os

#import hashlib



def getGray(image_file):
    tmpls = []
    for h in range(0, image_file.size[1]):  # h
        for w in range(0, image_file.size[0]):  # w
            tmpls.append(image_file.getpixel((w, h)))
    return tmpls


def getAvg(ls):#获取平均灰度值
    return sum(ls) / len(ls)


def getMH(a,b):#比较64个字符有几个字符相同
    dist = 0;
    for i in range(0, len(a)):
        if a[i] == b[i]:
            dist = dist + 1
    return dist

def getImgHash(fne):
    image_file = Image.open(fne)  # 打开
    image_file = image_file.resize((12, 12))  # 重置图片大小我12px X 12px
    image_file = image_file.convert("L")  # 转256灰度图
    Grayls = getGray(image_file)  # 灰度集合
    avg = getAvg(Grayls)  # 灰度平均值
    bitls = ''  # 接收获取0或1
    # 除去变宽1px遍历像素
    for h in range(1, image_file.size[1] - 1):  # h
        for w in range(1, image_file.size[0] - 1):  # w
            if image_file.getpixel((w, h)) >= avg:  # 像素的值比较平均值 大于记为1 小于记为0
                bitls = bitls + '1'
            else:
                bitls = bitls + '0'
    return bitls

'''
 m2 = hashlib.md5() 
 m2.update(bitls)
 print m2.hexdigest(),bitls
 return m2.hexdigest()
'''

def foundimage(filePath):
    a = getImgHash("./Test2/测试图片.png")  # 图片地址自行替换
    files = os.listdir(filePath)  # 图片文件夹地址自行替换
    # print('files=', files)

    for file in files:
        number1 = file.find(".png")
        number2 = file.find(".")
        number3 = file.find("x.png")

        # if number3 == -1:
        #     print('文件---=',file)


        if number1 > 0 : # & number3 == -1
            b = getImgHash(filePath + "/" + str(file))
            compare = getMH(a, b)
            if compare > 90 :
                print(file, u'相似度', str(compare) + '%')

        if number2 == -1:
            foundimage(filePath+"/" + str(file))





foundimage("/Users/frank/Desktop/天跃科技项目文件/UI")

# ./Test
# /Users/frank/Desktop/天跃科技项目文件/UI