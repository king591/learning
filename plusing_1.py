#累加算术2
#设x为起点,i为固定间隔,t为累加次数,z为x按照间隔i递增累加t次的结果,求z
x = int(input("enter starting x:"))
i = int(input("enter i:"))
t = int(input("enter times t:")) - 1
z = x
while t != 0 :
    z = z + x + i
    x += i
    t -= 1
print (z)
