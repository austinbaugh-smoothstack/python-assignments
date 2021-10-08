#!/bin/python3
print("1)")
num1 = 50+50
print("50+50       = %d" % num1)
num2 = 100-10
print("100-10      = %d" % num2)

print("2)")
num3 = 30*+6
print("30*+6       = %d" % num3)
num4 = 6^6
print("6^6         = %d" % num4)
num5 = 6**6
print("6**6        = %d" % num5)
num6 = 6+6+6+6+6+6
print("6+6+6+6+6+6 = %d" % num6)

print("3)")
print("Hello World")
print("Hello World : 10")

print("4)")
def mortgage(debt, interest, months):
    for _month in range(1, months):
        debt += debt * (interest / 12) * 0.01
    return debt / months
print("input data")
loan = 800000
interest = 6
months = 103
print("%d %d %d" % (loan, interest, months))

print("answer:")
answer = mortgage(loan, interest, months)
print(answer)
