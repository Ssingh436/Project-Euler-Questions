import math

def product():
    for i in range(1,400):
        for j in range(1,400):
            k= math.sqrt(math.pow(i,2)+math.pow(j,2))
            if k == int(k):
                if i + j + k == 1000:
                    return (f'{i*j*k}, {i}, {j}, {k}')

print(product())