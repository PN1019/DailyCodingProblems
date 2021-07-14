

#This problem was asked by LinkedIn.

#Given a set of characters C and an integer k, a De Bruijn sequence is a cyclic sequence in which every possible k-length string of characters in C occurs exactly once.

#For example, suppose C = {0, 1} and k = 3. Then our sequence should contain the substrings {'000', '001', '010', '011', '100', '101', '110', '111'}, and one possible solution would be 00010111.

#Create an algorithm that finds a De Bruijn sequence.
# 
## Solution 1:
# find that euler path by starting at "0" * (n - 1)
# get to enumerate all the edges involving high numbers first
# get stuck at "0" * (n - 1), it would have already enumerated all edges of "0" * (n - 1) and all edges of the neighbors of "0" * (n - 1) and so on...
#For example , As I start from all [0] * (n-1), the loop should be from k-1 to 0(reverse loop). However, if I start from [k-1] * n, then the loop should be from 0 to k-1.
def deBruijnseq(self, n: int, k: int) -> str:
        visited = set()
        s = '0'*(n-1)# euler path
        res = s
        while True:
            for i in range(k-1,-1,-1):# trick here loop the reversed range
                if (s,i) not in visited:
                    res += str(i)
                    visited.add((s,i))
                    s = (s+str(i))[1:]
                    break
            else:
                return res

