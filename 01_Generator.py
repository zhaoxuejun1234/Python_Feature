def generator_test():
    while True:
        print("--1--")
        num = yield 100
        print("--2--", "num=", num)


g = generator_test()

# 第一次调用，会将yield 100执行完毕后暂停代码执行，注意此时 并没有给num值
print(next(g))
# print(next(g))
# print(next(g))

# send会让生成器从上次停止的位置 继续开始执行，并且会将11传递到生成器中
# 当做上一次执行yield 100 这个表达式的结果
# 然后在第4行代码，就可以想象成 num = 11了，因为100代表上次yield 100的结果
# 直到遇到下一次的yield 暂停运行，并且把100返回，此时就也打印了100
print(g.send(11))

# 与上次send(11)类似，只不过此次将22当做给yield 100这个表示的结果 给num
print(g.send(22))


