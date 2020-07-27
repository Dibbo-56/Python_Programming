while(True):
    n = int(input())
    if(n == 0):
        break
    while(not(n >= 0 and n <= 9)):
        d = n
        sum = 0
        while(not(d == 0)):
            sum += d % 10
            d = int(d/10)
        n = sum
    print(n)
