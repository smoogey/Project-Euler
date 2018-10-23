import math

def primeSieve(target):
    index = 2
    primeCounter = 0
    primes = list()
    sieve = [True for i in range(target**2)]
    while index <= target:
        if sieve[index] == True:
            for i in range(index * 2, target**2, index):
                sieve[i] = False
        index += 1
    targetReached = False
    while targetReached == False:
        for i in range(2, target**2):
            if sieve[i] == True:
                primes.append(i)
                primeCounter += 1
            if primeCounter == target:
                targetReached = True
                break
    return primes

print(primeSieve(11))