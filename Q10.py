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

def SumOfPrimes(m):
    total = 0
    for i in range(2,m):
        try:
            if memo[i] == True:
                total += i
        except:
            if isPrime(i) == True:
                total += i
    return total

print(SumOfPrimes(2000000))

