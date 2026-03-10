#Author: Brahmjot S.A.
#Date: 13/02/26
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
                    if n%i == 0:
                        memo[n] = False 
                        return False
            except:
                if isPrime(i):
                    if n%i == 0:
                        memo[n] = False
                        return False
    memo[n] = True
    return True

def LargestPrimeFactor(m):
    factor = 1
    end = int(math.sqrt(m))+1
    for i in range(2,end):
        if isPrime(i):
            if m%i==0 and i > factor:
                factor = i
    return factor

print(LargestPrimeFactor(600851475143))
