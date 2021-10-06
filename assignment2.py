#!/bin/python3
import re

print("1)")
string = "Hello World"
print(string[-3])

print("2)")
string = "thinker"
print(string[2:5])
string = "hello"
print(string[1])

print("3)")
string = "Sammy"
print(string[2:])

print("4)")
string = "Mississippi"
print(set(string))

print("5)")
strings = [
    "Stars",
    "O, a kak Uwakov lil vo kawu kakao!",
    "Some men interpret nine memos",
]
def is_palindrome(input):
    input = re.sub('[^a-z]+', '', input.lower())
    return input == input[::-1]
for string in strings:
    print(string)
    if(is_palindrome(string)):
        print("Y")
    else:
        print("N")

print("1)")
list = [13, "word", 1.5]
print(list)

print("2)")
list = [1, 1, [1, 2]]
print(list[2][1])

print("3)")
list = ['a', 'b', 'c']
print(list[1:])

print("4)")
dict = {
    'Sunday': 0,
    'Monday': 1,
    'Tuesday': 2,
    'Wednesday': 3,
    'Thursday': 4,
    'Friday': 5,
    'Saturday': 6,
}
print(dict)

print("5)")
dict = {
    'k1': [1, 2, 3],
}
print(dict['k1'][1])

print("6)")
list = [1, [2, 3]]
tup = (list[0], list[1][0], list[1][1])
print(tup)

print("7)")
string = "Mississippi"
print(set(string))

print("8)")
list.append('X')
print(list)

print("9)")
print(set([1, 1, 2, 3]))

print("Question 1)")
result = []
for i in range(2000, 3200):
    if i % 7 == 0 and i % 5 != 0:
        result.append(i)
print(result)

print("Question 2)")
def factorial(num):
    if num == 0:
        return 1
    return num * factorial(num - 1)
num = 8
print(factorial(num))

print("Question 3)")
def build_dict(num, result):
    result[num] = num * num
    if num == 1:
        return result
    return build_dict(num - 1, result)
print(build_dict(8, {}))

print("Question 4)")
l=[1,2,3]
t=tuple(l)
print(l)
print(t)

print("Question 5)")
class Object:
    def __init__(self):
        self.s = ""
    def getString(self, str):
        self.s = str
    def printString(self):
        print(self.s.upper())
obj = Object()
obj.getString("some sting")
obj.printString()

def crowd_test(crowd):
    if len(names) > 3:
        print("3 is a crowd")

print("Three is a Crowd:")
names = [ "Bob", "Alice", "Onizuka", "Bowser" ]
crowd_test(names)
names.remove("Onizuka")
names.remove("Bowser")
crowd_test(names)

print("Three is a Crowd - Part 2:")
def crowd_test(crowd):
    if len(names) > 3:
        print("3 is a crowd")
    else:
        print("the room is not very crowded")
crowd_test(names)

print("Six is a Mob:")
names = [ "Bob", "Alice", "Onizuka", "Bowser", "Iris", "Ed" ]
def crowd_test(crowd):
    if len(names) > 5:
        print("mob in the room")
    elif len(names) > 2:
        print("3 is a crowd")
    elif len(names) > 0:
        print("the room is not very crowded")
    else:
        print("the room is empty")
crowd_test(names)
