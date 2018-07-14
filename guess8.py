#-*- coding: utf-8 -*

#引入 random 模块
import random
#声明模块中的变量
answer = random.randint(1,10)
print("第一个case")
temp = input("你猜一下1-10间的数字：")
guess = int(temp)
t = 0
while guess != answer:
    t = t + 1
    guess = int(temp)
    if guess > answer:
        temp = input("很抱歉，猜大了，小一点试试？：" + "你还剩下" + str(10 - t) + "次机会哦！")
        if t == 9:
            print("不好意思，没机会了，花五毛再来吧")
            break
    elif guess < answer: 
        temp = input("很抱歉，猜小了，换个大一点的数字吧：" + "你还剩下" + str(10 - t) + "次机会哦！")
        if t == 9:
            print("不好意思，没机会了，花五毛再来吧")
            break
    else:
        break
if guess == answer:
    print("恭喜你！猜对了 " + "哈哈哈哈")
    print("Game Over!正确答案是：" + str(answer))
