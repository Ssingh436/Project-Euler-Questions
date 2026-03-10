#Date: 21/02/26 

def isPalindrome(n):
    num = str(n)
    length = len(num)
    if length%2 == 0:
        L = num[:length//2]
        R = num[length//2:]
    else:
        L = num[:length//2]
        R = num[length//2+1:]
    for i in range(length//2):
        if L[i] != R[length//2-1-i]:
            return False
    return True

def LargestPalindromeProductN(n):
    palindrome = 0
    for i in range (10**(n-1), 10**n):
        for j in range (10**(n-1), 10**n):
            if isPalindrome(i*j) and i*j > palindrome:
                palindrome = i*j
    return palindrome

print(LargestPalindromeProductN(4))


        
