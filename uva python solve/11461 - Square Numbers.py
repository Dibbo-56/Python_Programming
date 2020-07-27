import math

while (True):
    a, b = map(int, input().split())
    if(a == 0 and b == 0):
        break
    print(math.floor(math.sqrt(b)) - math.ceil(math.sqrt(a)) + 1)
