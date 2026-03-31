#Date: 26/02/26
import math 

# Dictionary to store primes to reduce waste of computer resources
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

def nthPrime(n):
    count = 0
    # using upper bound for n greater than or equal to 6
    for i in range(2, math.ceil(n*(math.log(n)+ math.log(math.log(n))))):
        if isPrime(i):
            count += 1
        if count == n:  
            return i
        

print(nthPrime(10001))