def  square(L):
    a = L/4
    s = a **  2
    return s

x = int(input('请输入正方形的周长：'))
y = square(x)
print('正方形的面积是：',y)
