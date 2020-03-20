#文件
#打开文件
#file_name = 'C:/Users/becky/Desktop/demo.txt'
file_name = r'C:\Users\becky\Desktop\demo.txt' #原始字符串
file_obj = open(file_name) #打开对应文件
print(file_obj)
#read()方法读取文件内容，会将内容保存为一个字符串返回
#content = file_obj.read()
#print(content)

#关闭文件
#file_obj.close()

#with ... as 语句
try:
    #调用open()打开一个文件，可以分为两种类型
    #一种是纯文本文件（使用utf-8编码）
    #一种是二进制文件（图片，MP3，ppt等）
    # open()打开文件时默认是以文本形式打开的，但是open()默认的编码是none
    with open(file_namew,encoding='UTF-8') as file_obj:
        print(file_obj.read())
except FileNotFoundError:
    print(f'{file_name}文件不存在')

