#same logic as solution.java but not accepted due to TLE.

from math import sqrt

def checkPrime(num):
    for i in range(2, int(sqrt(num)) +1):
        if(num%i == 0):
            return False
    return True
    
n = 1000000000

testcases = int(input())

for _ in range(testcases):
    L, R = map(int,list(str(input()).split()))
    if(L == 1):
        L = 2
    for i in range(L, R+1):
        if( i%6 == 1 or i%6 == 5 or i == 2 or i == 3 ):
            if(checkPrime(i)):
                print(i)
    print()
