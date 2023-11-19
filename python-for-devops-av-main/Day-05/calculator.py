import sys

def addition():
    add = num1 + num2
    print(add)

def subtraction():
    sub = num1 - num2
    print(sub),

num1 = float(sys.argv[1])
operation = sys.argv[2]
num2 = float(sys.argv[3])

if operation == 'add':
    addition()

if operation == 'sub':
    subtraction()