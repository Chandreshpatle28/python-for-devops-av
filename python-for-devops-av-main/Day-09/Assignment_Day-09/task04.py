## `continue` Statement

#The "continue" statement is used to skip the current iteration of the loop and 
#   proceed to the next one. It can be used in both "for" and "while" loops, 
#   enabling you to bypass certain iterations based on a condition.

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
for number in numbers:
    if number == 5:
        continue
    print(number)