# This code finds the largest palindrome that is the product of two three digit numbers. 

import math

# reverse the list range(minNum,1000)

def reverseList(minNum):
    nums = []
    for i in reversed(range(minNum,1000)):
        nums.append(i)
    return nums

# makes a list of the digits of a number 100000 <= x <= 999999

def digits(num):
    digitList = []
    if 100000 <= num <= 999999:
        power = 5
        tempNum = num
        while power >= 0:
            digit = int(tempNum / 10 ** power)
            digitList.append(digit)
            tempNum = tempNum - digit* 10**power
            power = power - 1
    return digitList

# Reverses the digits of a number.

def reverse(num):
    digitList = digits(num)
    revDigitList = []
    for i in reversed(digitList):
        revDigitList.append(i)
    return revDigitList

print(reverse(123456))
    
# compares the digits and reversed digits of a number 100000 <= x <= 999999

def compare(num):
    check = None
    if digits(num) == reverse(num):
        check = True
    else:
        check = False
    return check

# Checks multiples from reverse(minNum) to find palindromes.

def palindrome(minNum):
    palindromes = []
    for i in reverseList(minNum):
        for j in reverseList(minNum):
            if compare(i * j):
                palindromes.append(i * j)
    return(palindromes)

print(max(palindrome(900)))
