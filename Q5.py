#Date: 21/02/26

memo = {}

def HCF(n,m):
    if n ==m:
        return n
    elif n == 1:
        return 1
    elif m == 1:
        return 1
    smaller =  m if n > m else n
    factor = 1
    for i in range(2, smaller+1):
        if m % i == 0 and n % i == 0:
            factor = i if i>factor else factor
    return factor

def SmallestEvenlyDivisible(n):
    if n == 1:
        memo[n] = 1
        return 1
    elif n == 2:
        memo[n] = 2
        return 2
    else:
        try:
            last = memo[n-1]
        except:
            last = SmallestEvenlyDivisible(n-1)
        print(last)
        memo[n] = last*n // HCF(last, n)
        return memo[n]
        
print(SmallestEvenlyDivisible(20))