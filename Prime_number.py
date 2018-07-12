# -*- coding:utf-8 -*

import math
n = float(input("请输入一个正整数："))
# 判断n是否为正整数，如果是，将n转为整型数值
N = math.modf(n) #将n转为浮点型，并分开整数和小数部分
ver = 1
while ver == 1 :
    if N[0] != 0 or n <= 0 : #判断：小数部分是否等于0，或整数部分是否小等于0
        n=float(input("这不是一个正整数，请输入一个正整数："))
        N = math.modf(n)
    else :
        n = int(n)
        ver += 1

#判断n是否为素数(即能否被1和n以外的正整数整除，2～n-1)    
t = 2
while t < n : #从2~n-1找一个小于n的数t
    if n%t != 0 : #一个小于n的数不能整除n
        t += 1
    else : #一个小于n的数可以整除n
        print(n,"是一个合数")
        break
else :
    print(n,"是一个素数")
