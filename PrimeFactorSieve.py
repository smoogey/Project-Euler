import math

n = 600851475143  # Number to be considered.


# Reduces number so that primes list isn't too large for processor.

def numRed(num):
    while num >= 100000:
        num = int(math.sqrt(num) + 1)
    return num


# Makes a list of primes up to a reduced x

def getPrimes(x):
    primes = [2]
    p = 3

    while p <= numRed(x) + 1:
        primes.append(p)
        p += 2

    for i in primes:
        for j in primes:
            if i != j and j % i == 0:
                primes.remove(j)

    return primes


# Makes a list of prime factors of a reduced x

def getFactors(x):
    primes = getPrimes(x)
    factors = []

    for i in primes:
        if x % i == 0:
            factors.append(i)

    return factors


print(getFactors(n))


# Makes a list of prime factors for x.

def factor(x):
    factors = getFactors(x)
    allFactors = []

    while x > 1:
        while x % max(factors) == 0:
            x = x / max(factors)
            allFactors.append(max(factors))
        factors = getFactors(x)

    return sorted(allFactors)


print(factor(99999))