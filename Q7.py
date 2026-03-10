#Author: Brahmjot S.A.
#Date: 26/02/26
import numpy as np
import math 
memo = {}

def isPrime(n):
    try:
        if memo[n]:
            return True
    except:
        end = int(math.sqrt(n))+1
        for i in range(2, end):
            try:
                if memo[i]:
                    if n%i == 0 and n != i:
                        memo[n] = False 
                        return False
            except:
                if isPrime(i):
                    if n%i == 0 and n != i:
                        memo[n] = False
                        return False
    memo[n] = True
    return True

primes = {1:2}

def nthPrime(n):
    if n == 1 :
        return 2
    try:
        onebeforenthp = primes[n-1]
    except:
        onebeforenthp = nthPrime(n-1)
    for i in range(onebeforenthp, 2*onebeforenthp+1):
        if isPrime(i) and i != 2:
            print(f'Prime is {i}')
            primes[len(primes)+1] = i
    print(primes[n])
    return(primes[n])
nthPrime(3)
print(primes[3])
