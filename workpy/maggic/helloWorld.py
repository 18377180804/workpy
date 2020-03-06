#!/usr/bin/python
# -*- coding: UTF-8 -*-

name="hello world"
print("你好",1+1)

#定义初始值
# start=1
# while True:
# #判断start的值若其为51，则说明上一次已经输出了100，跳出循环
#    if start==51:
#      break
#    print(start*2)
#    start +=1

# print("计算 1+2+...+100 的结果为：")
# #保存累加结果的变量
# result = 0
# #逐个获取从 1 到 100 这些值，并做累加操作
# for i in range(101):
#     result += i
# print(result)

a=1;
while a<10:
    print("a=",a)
    a +=2


b=1
while b<11:
    if(b%2 ==0):
        print(b,"是偶数")
    else:
        print(b,"是基数")
    b +=1

def diguisuanfa(list):
    if list[1:]:
        print("啥啥啥")
        return 1+diguisuanfa(list[1:])
    else:
        print("hshaha")
        return 1


line = [1, 2, 3, 4, 5, 2, 7]
diguisuanfa(line)





