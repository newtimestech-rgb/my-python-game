import random

print("🎮 欢迎来到升级版的猜数字游戏！")

# 电脑随机生成一个 1 到 10 的数字
secret_number = random.randint(1, 10)

# 核心：使用 while 循环，让玩家可以一直猜，直到猜对为止
while True:
    guess = int(input("请猜一个 1 到 10 之间的数字："))

    # 条件判断逻辑
    if guess == secret_number:
        print("🎉 太厉害了！终于猜对了！游戏结束！")
        break  # 使用 break 跳出循环，结束游戏
    elif guess > secret_number:
        print("📈 猜大了哦！再试一次：")
    else:
        print("📉 猜小了哦！再试一次：")
