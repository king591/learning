#累加算术
#设x为起点,y为终点,i为固定间隔,z为x到y的累加,求z
x = int(input("enter starting x:"))
y = int(input("enter ending y:"))
i = int(input("enter i:"))
z = x
t = 0
while x < y :
    z = z + x + i
    x += i
    t += 1
print (z)
