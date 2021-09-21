# This problem was asked by Indeed.[Medium]

# Given a 32-bit positive integer N, determine whether it is a power of four in faster than O(log N) time.

# Solution by using log and floor:

from math import log, floor
 
 
# Returns true if `n` is a power of four
def checkPowerOf4(n):
 
    # find `log4(n)`
    i = log(n) / log(4)
 
    # return true if `log4(n)` is an integer
    return i == floor(i)
 
 
if __name__ == '__main__':
 
    n = 256
 
    if checkPowerOf4(n):
        print(n, 'is a power of 4')
    else:
        print(n, 'is not a power of 4')
# Solution By Bit Manipulation :
# Returns true if `n` is a power of four
def checkPowerOf4(n):
 
    # return true if `n` is a power of 2, and its only
    # set bit is present at even position
    return n and not (n & (n - 1)) and not (n & 0xAAAAAAAA)
 
 
if __name__ == '__main__':
 
    n = 256
 
    if checkPowerOf4(n):
        print(n, 'is a power of 4')
    else:
        print(n, 'is not a power of 4')
#Solution By PowerOf4:

# Returns true if `n` is a power of four
def checkPowerOf4(n):
 
    # return true if `n` is a power of 2, and
    # the remainder is 1 when divided by 3
    return ((n & (n - 1)) == 0) and (n % 3 == 1)
 
 
if __name__ == '__main__':
 
    n = 256
 
    if checkPowerOf4(n):
        print(n, 'is a power of 4')
    else:
        print(n, 'is not a power of 4')
 
