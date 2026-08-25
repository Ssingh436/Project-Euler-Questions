import math

def nth_triangle(n):
    return n*(n+1)//2

def n_divisors(num):
    divisors = 0
    for i in range(1,math.ceil(math.sqrt(num+1))):
        if num%i == 0:
            divisors += 2
    return divisors

def first_tri_over_n(n):
    divisors = 0
    triangle = 0
    while divisors <= n:
        triangle +=1
        divisors = n_divisors(nth_triangle(triangle))
    return nth_triangle(triangle)

print(first_tri_over_n(500))

