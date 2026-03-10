#Author: Brahmjot S.A.
#Date: 13/02/26
memo = {}

def FibonnaciNum(n):
    if n == 1:
        memo[n] = 1
        return 1
    elif n==2:
        memo[n] = 2
        return 2
    else:
        try:
            memo[n] = memo[n-2]
        except:
            memo[n] = FibonnaciNum(n-2)
        try:
            memo[n] += memo[n-1]
        except:
            memo[n] += FibonnaciNum(n-1)


        return memo[n]

def EvenFibonnaciSum(m):
    sum = 0 
    count = 0
    while True:
        count += 1
        if FibonnaciNum(count)%2 ==0:
            sum += FibonnaciNum(count)
        if FibonnaciNum(count)> m:
            if FibonnaciNum(count)%2 == 0:
                sum -= FibonnaciNum(count)
            break
    return sum
print(EvenFibonnaciSum(4000000))

# Answer is 4,613,732
        

    

        
