import math
import time

def primeSieve(target):
    index = 2
    primeCounter = 0
    primes = list()
    sieve = [True for i in range(target**2)]
    for index in range(2, target):  #changed to range instead of manually incrementing index
        if sieve[index]:
            for i in range(index * 2, target**2, index):
                sieve[i] = False
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

startTime = int(round(time.time() * 1000))
print(primeSieve(44))
endTime = int(round(time.time()) * 1000) - int(startTime)
print("Prime Sieve took " + str(endTime) + " milliseconds.")