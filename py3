import math

bigNum = 600851475143

# Finds the prime the factors of a given number.
def primeFact(num):
    p = 2
    factors = []
    tempNum = num
    if num % 2 == 0:
        while tempNum % 2 == 0:
            tempNum = tempNum / 2
            factors.append(2)
    p = 3
    while tempNum >= math.sqrt(num) +10:
        if tempNum % p == 0:
            while tempNum % p == 0:
                tempNum = tempNum / p
                factors.append(p)
        p += 2
    factors.append(tempNum)
    return factors


print(primeFact(bigNum))

#Finds the largest prime factor of a number.
def bigFact(num):
    return max(primeFact(num))

print(bigFact(bigNum))
