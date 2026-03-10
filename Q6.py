#Date: 21/02/26


# Use the fact that the sum from r=1 to r=n of r^2 = n(n+1)(2n+1)//6
def SumOfSquares(n):
    return n*(n+1)*(2*n+1)//6

#Use the fact that the sum from r=1 to r=n of r = n(n+1)//2. The square of this sum is actually the sum of r^3
def SquareOfSums(n):
    return ((n)*(n+1)//2)**2

def DiffSumSquaresAndSquareSums(n):
    return SquareOfSums(n) - SumOfSquares(n)

print(DiffSumSquaresAndSquareSums(100))