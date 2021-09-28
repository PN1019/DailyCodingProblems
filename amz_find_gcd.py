#This problem was asked by Amazon.[EASY}

#Given n numbers, find the greatest common denominator between them.

#For example, given the numbers [42, 56, 14], return 14.
#Solution using numpy
import numpy as np

A = [14,56,42]

print(np.gcd.reduce(A))

#Solution: Scaling for any number of input values
n = int(input('HOW MANY NUMBERS YOU WANT TO CALCULATE GCD?: '))
a = list(map(int,input('ENTER THE NUMBER TO COMPUTE GCD: ').strip().split()))[:n]

def compute_gcd(num1,num2):
    x = 1
    while x:
        if max(num1,num2) % min(num1,num2) == 0:
            return min(num1,num2)
            x = 0
        else :
            r = max(num1,num2)%min(num1,num2)
            return compute_gcd(max(num1,num2),r)

while True:
        a[0] = compute_gcd(a[0],a[1])
        a.pop(1)
        if len(set(a))>2:
            a.pop(2)
        if len(set(a)) == 1:
            break
a = set(a)
print(f"GCD OF {n} NUMBERS IS {a}")

#Solution by Euclidean algo
def compute_gcd(x, y):
     
    while(y):
        x, y = y, x % y
     
    return x
         
# Driver Code       
l = [ 42, 56, 14]
 
num1 = l[0]
num2 = l[1]
gcd = compute_gcd(num1, num2)
 
for i in range(2, len(l)):
    gcd = compute_gcd(gcd, l[i])
     
print(f"the gcd among the numbers {l} is {gcd}")

#Solution using functools:

import functools as f
A = [56, 42, 14]
g = lambda a,b:a if b==0 else g(b,a%b)   #Gcd for two numbers
print(f.reduce(lambda x,y:g(x,y),A))     #Calling gcd function throughout the list.
