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
