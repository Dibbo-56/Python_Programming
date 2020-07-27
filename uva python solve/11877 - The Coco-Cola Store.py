while(True):
    n = int(input())
    if(n == 0):
        break
    s = 0
    while(n >= 3):
        s += int(n/3)
        n = int(n / 3) + (n % 3)
    if(n == 2):
        s += 1
    print(s)
