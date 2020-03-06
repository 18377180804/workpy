# !/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import json

bait_type_path = os.path.dirname(__file__)

# f=open(os.path.join(bait_type_path, "date.json"),"r",encoding="utf-8")
# f1=open(os.path.join(bait_type_path, "nonull.txt"),"w")
# f2=open(os.path.join(bait_type_path, "null.txt"),"w")


f4=open('C:\\Users\\zxc\Desktop\\filternull\\filter.txt','r',encoding='utf-8')
f4str=f4.read().split(',')




f=open('C:\\Users\\zxc\Desktop\\filternull\\date.json','r',encoding='utf-8')
f1=open("C:\\Users\zxc\Desktop\\filternull\\nonull.txt","w")
f2=open("C:\\Users\zxc\Desktop\\filternull\\null.txt","w")

for line in f:
    linedict=json.loads(line)
    tid=linedict["organizeID"]

    listline=[]
    for fline in f4str:
        listline.append(linedict[fline])


    if '' in listline:
        print("nullll",tid)
        f2.write(line)
    else:
        print("nonull---",tid)
        f1.write(line)