def SumOfMultiples(a, b, limiter):
    count = 0
    for i in range(1, limiter):
        if i % a == 0 or i % b == 0:
            count += i
    return count

def FasterSumOfMultiples(a, b, limiter):
    count = 0
    count += ((a + (a*(limiter//a)))/2)*(limiter//a)
    count += ((b + (b*(limiter//b)))/2)*(limiter//b)
    count -= (((a*b) + ((a*b)*(limiter//(a*b))))/2)*(limiter//(a*b))
    return int(count)

print(FasterSumOfMultiples(3,5,1000))
print(SumOfMultiples(3,5,1000 ))
