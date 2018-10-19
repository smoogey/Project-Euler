import time
import math

#This file finds the prime factors of 'n' by doing finding each next prime and trying to divide the operand by the prime
#If operand%prime==0, keep dividing until that's not the case, add the prime to the list and find the next prime until
#prime >= operand.

n=300000

def findFactorPrimes(factoree):

    primeList = [2,3]
    factorList = list()

#TODO: add 2, and 3 checking.
    for primeCandidate in range(5,factoree,2):
        primeListIteration = list(primeList)
        isPrime = True
        for prime in primeListIteration:
            if prime > math.ceil(math.sqrt(primeCandidate)) or isPrime == False:
                break
            if not primeCandidate % prime:
                # print("Not Prime found: " + str(primeCandidate))
                isPrime = False
        if isPrime == True:
            primeList.append(primeCandidate)
            while not factoree % primeCandidate:
                print("Prime Factor found: " + str(primeCandidate))
                factorList.append(primeCandidate)
                factoree = factoree / primeCandidate

    #TODO: cull dups

    return factorList

preMillis = int(round(time.time() * 1000))
print("Testing getFactors function:" + str(findFactorPrimes(n)))
print("Time to finish in millis: " + str(int(round(time.time() * 1000 )) - preMillis))