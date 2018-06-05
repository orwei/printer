# encoding: UTF-8
import base64        #导入库
f=open("logo.bmp",'rb')   #打开图片
print(f.read())
mystr=base64.b64encode(f.read()) #读取图片内容，并按base64编码
# print(mystr)
f.close()  #关闭打开的图片文件
f=open("aaa.txt",'wb')  #打开文本文件
f.write(mystr)   #写入刚才编码的内容
f.close()  #关闭打开的文本文件。