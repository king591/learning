# -*- coding:utf-8 -*

#创建一个函数：判断正整数
def int_check(n) :
    import math
    n = float(n)
    # 判断n是否为正整数，如果是，将n转为整型数值
    N = math.modf(n) #将n转为浮点型，并分开整数和小数部分
    ver = 1
    while ver == 1 :
        if N[0] != 0 or n <= 0 : #判断：小数部分是否等于0，或整数部分是否小等于0
            return False
        else :
            ver += 1
            return True
#创建一个函数：判断正整数是否为素数
def is_prime(p) :
    # for 写法有点问题：
    # for t in range(2,p) :
    #     if p % t == 0 :
    #         if t < p:
    #             return False
    #         else :
    #             return True
    #     else :
    #         return True
    t = 2
    while t < p : #从2~p-1找一个小于n的数t
        if p % t != 0 : #一个小于n的数不能整除n
            t += 1
        else : #一个小于n的数可以整除n
            return False
    else :
        return True

n = input('请输入一个正整数')

#调用函数判断正整数
i = 1
while i == 1 :
    if int_check(n) == False :
        n=input("这不是一个正整数，请输入一个正整数：")
    else :
        n = int(n)
        i += 1

#while写法：判断n是否为素数(即能否被1和n以外的正整数整除，2～n-1)
t = 2
while t < n : #从2~n-1找一个小于n的数t
    if n%t != 0 : #一个小于n的数不能整除n
        t += 1
    else : #一个小于n的数可以整除n
        print('while写法:',n,"是一个合数")
        break
else :
    print('while写法:',n,"是一个素数")


if is_prime(n) :
    print('while公式写法：',n,'是一个素数')
else :
    print('while公式写法：',n,'是一个合数')
