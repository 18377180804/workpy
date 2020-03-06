# !/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import json


bait_type_path = os.path.dirname(__file__)

f4=open(os.path.join(bait_type_path, "filter.txt"),'r',encoding='utf-8')
f=open(os.path.join(bait_type_path, "date.json"),"r",encoding="utf-8")
f1=open(os.path.join(bait_type_path, "nonull.txt"),"w",encoding="utf-8")
f2=open(os.path.join(bait_type_path, "null.txt"),"w",encoding="utf-8")


# f4=open('C:\\Users\\zxc\Desktop\\filternull\\filter.txt','r',encoding='utf-8')
# f=open('C:\\Users\\zxc\Desktop\\filternull\\date1.json','r',encoding='utf-8')
# f1=open("C:\\Users\zxc\Desktop\\filternull\\nonull.txt","w",encoding="utf-8")
# f2=open("C:\\Users\zxc\Desktop\\filternull\\null.txt","w",encoding="utf-8")

f4str=f4.read().split(',')

for line in f:
    linedict=json.loads(line)

    listline=[]
    for fline in f4str:
        if (fline in line) :
            listline.append(linedict[fline])
        else:
            listline.append('')


    if '' in listline or None in listline:
        f2.write(line)
        print('null---')
    else:
        f1.write(line)
