# username = "chaiaurcode"

# def test():
#     username = "chai"
#     print(username)

# test()
# print(username)


x = 99
# def func(y):
#     z = x+y
#     return z

# result = func(55)
# print("Result: ", result)


# def func2():
#     global x
#     x = 88

# func2()
# print(x)


# def f1():
#     x= 12
#     def f2():
#         print(x)
#     return f2

# myFunc = f1()
# myFunc()

def f1(num1):
    def f2(num2):
        return num2**num1
    return f2

f = f1(2)
g = f1(3)

print(f(4))
print(g(4))