#!/usr/bin/python
# -*- coding: UTF-8 -*-


f =open('C:\\Users\\zxc\\Desktop\\date.json','r',encoding='utf-8')
# f.write('sssss')
# f.close()
# f =open('C:\\Users\\zxc\\Desktop\\date.json','r',encoding='utf-8')
str = f.read()

f.close()


with open('C:\\Users\\zxc\\Desktop\\date.json',"r") as f:
    line1 = f.readline()    #可以是随便对文件的操作
    print("=-------",line1)

data=[]
for line in open('C:\\Users\\zxc\\Desktop\\date.json',"r") :
    line=line[:-1]
    data.append(line)

print("date==",data)