import time
import math

#This file finds the prime factors of 'n' by dividing the operand by each number. If operand%candidate==0,
#keep dividing until its no longer the case, add candidate to list of factors and keep going with new operand until
#candiate >= sqrt(operand)

n=600851475145697


def createFactorList(factoree):
    factorList = list()

    while not factoree % 2:
        factorList.append(2)
        factoree = int(factoree / 2)

    for factorCandidate in range(3, factoree, 2):
        if factorCandidate >= math.ceil(math.sqrt(factoree)):
            factorList.append(factoree)
            return factorList
        if factoree == 1:
            return factorList

        while not factoree % factorCandidate:
            factorList.append(factorCandidate)
            factoree = int(factoree / factorCandidate)


def findFactorPrimes(factoree):
    factorList = createFactorList(factoree)
    nonDupeFactorList = []

    for item in factorList:
        if not item in nonDupeFactorList:
            nonDupeFactorList.append(item)

    return nonDupeFactorList

preMillis = int(round(time.time() * 1000))
print("Testing getFactors function:" + str(findFactorPrimes(n)))
print("Time to finish in millis: " + str(int(round(time.time() * 1000 )) - preMillis))
