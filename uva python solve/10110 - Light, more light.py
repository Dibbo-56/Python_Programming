import math

while(True):
    n = int(input())
    if(n == 0):
        break
    r = int(math.sqrt(n))
    if(r*r == n):
        print("yes")
    else:
        print("no")
