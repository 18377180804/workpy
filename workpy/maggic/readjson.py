# !/usr/bin/python
# -*- coding: UTF-8 -*-
import json

f =open('C:\\Users\\zxc\\Desktop\\date.json','r',encoding='utf-8')
jsonstr=f.read()

print(jsonstr)
print('--------------------------------------')



f1=open("C:\\Users\\zxc\\Desktop\\guolv.txt","w")
f2=open("C:\\Users\\zxc\\Desktop\\guolvnull.txt","w")
for line in open('C:\\Users\\zxc\\Desktop\\date.json','r',encoding='utf-8'):
    # linejson=json.dumps(line)
    linedict=json.loads(line)

    tid=linedict["organizeID"]
    print("tdd----",tid)

    if  ''.__eq__(tid):
        print("nullll",tid)
        f2.write(line)
    else:
        print("nonull---",tid)
        f1.write(line)









