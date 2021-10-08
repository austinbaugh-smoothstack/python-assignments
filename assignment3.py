#!/bin/python3
import random

print("1)")
nums = []
for num in range(1500, 2700):
    if num % 7 == 0 and num % 5 == 0:
        nums.append(num)
print(nums)

print("2)")
def convert_temp(to_celcius, og_temp):
    if to_celcius:
        return (og_temp-32)*5/9
    return (og_temp*9/5)+32
print(convert_temp(False, 60))
print(convert_temp(True, 45))

print("3)")
num = random.randrange(1,10)
while True:
    guess = input("Guess a number between 1 and 9: ")
    if int(guess) == num:
        print("Well guessed!")
        break

print("4&5)")
for h in range(1,10):
    row = ""
    if h > 5:
        h = 10 - h
    for w in range(0,h):
        row += " *"
    print(row)

print("6)")
word = input("Provide a word: ")
print("Reversed: " + word[::-1])

print("7)")
num_evens = num_odds = 0
for num in range(1, 10):
    if num % 2 == 0:
        num_evens += 1
    else:
        num_odds += 1
print("Number of even numbers: " + str(num_evens))
print("Number of odd numbers: " + str(num_odds))

print("8)")
list = [
    1452,
    11.23,
    1+2j,
    True,
    'w3resource',
    (0, -1),
    [5, 12],
    {"class": 'V', "section":'A'}
]
for item in list:
    print("Value: " + str(item))
    print("Type: " + str(type(item)))

print("9)")
nums = []
for num in range(0,6):
    if num != 3 and num != 6:
        nums.append(num)
print(nums)
