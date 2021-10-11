#!/bin/python3
print("4_a)")
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

print("10)")
def func10(n1, n2):
    if n1 % 2 == 0 and n2 % 2 == 0:
        return min(n1, n2)
    return max(n1, n2)
print(func10(4, 2))
print(func10(4, 3))
print(func10(5, 3))

print("11)")
def same_first_char(str1, str2):
    return str1[0] == str2[0]
print(same_first_char("apple", "banana"))
print(same_first_char("apple", "art"))

print("12)")
def func12(value):
    return (value - 7) * 2 + 7
print(func12(7))
print(func12(6))
print(func12(8))
print(func12(5))
print(func12(9))

print("13)")
def func13(string):
    return string[0].upper() + string[1:4] + string[4].upper() + string[5:]
print(func13("string"))

print("4_b)")
print("1)")
orders = [
    [ 34587, "Learning Python, Mark Lutz", 4, 40.95 ],
    [ 98762, "Programming Python, Mark Lutz", 4, 56.8 ],
    [ 77226, "Head First Python, Paul Barry", 3, 32.95 ],
    [ 88112, "Einführung in Python3, Bernd Klein", 3, 24.99 ],
]
print(orders)

print("2)")
def order_prices(orders):
    '''
    Returns list of tuples, containing the order number and total price
    '''
    return list(map(lambda order: (order[0], order[2] * order[3]), orders))
print(order_prices(orders))

print("3)")
orders = [
    [ 77226, (7,  3, 32.95), (13, 4, 56.8), (13, 4, 56.8) ],
    [ 34587, (45, 4, 40.95), (45, 4, 40.95) ],
    [ 88112, (27, 3, 24.99), (13, 4, 56.8) ],
    [ 98762, (13, 4, 56.8) ],
]
def order_prices(orders):
    '''
    Returns list of tuples, containing the order number and total price
    '''
    def total_price(article):
        (_, q, p) = article
        return q * p
        
    return list(
        map(
            lambda order: (
                order[0],
                sum(list(map(total_price, order[1::])))
            ),
            orders
        )
    )
print(order_prices(orders))
