#!/bin/python3
"""
print("1)")
def func():
    print("Hello World")
func()

print("2)")
def func1(name):
    print("Hello my name is " + name)
func1("Google")

print("3)")
def func3(x,y,z):
    if z:
        return x
    return y
print(func3("hello", "goodbye", False))

print("4)")
def func4(x,y):
    return x * y
print(func4(2,3))

print("5)")
def is_even(num):
    return num % 2 == 0
print(is_even(3))

print("6)")
def func6(x,y):
    return x > y

print("7)")
def args_sum(*args):
    return sum(args)
print(args_sum(1, 2, 3))

print("8)")
def even_args(*args):
    return list(filter(lambda arg: arg % 2 == 0, list(args)))
print(even_args(1, 2, 3, 4))

print("9)")
def func9(string):
    result = ""
    for (i, c) in enumerate(string):
        if i % 2 == 0:
            result += c.upper()
        else:
            result += c.lower()
    return result
print(func9("test"))
"""

print("10)")
