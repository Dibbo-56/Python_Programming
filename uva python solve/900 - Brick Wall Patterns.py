while(1):
    n = int(input())
    if(n == 0):
        break
    elif(n == 1):
        print(1)
    elif(n >= 2):
        f1, f2 = 1, 1
        for i in range(n):
            f = f1 + f2
            f1 = f2
            f2 = f
        print(f1)
