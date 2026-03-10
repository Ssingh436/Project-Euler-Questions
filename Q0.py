
def SumOfOddSquares(n):
    sum = 0
    for i in range (1,n,2):
        sum += i*i
    return sum

print(SumOfOddSquares(800000))
