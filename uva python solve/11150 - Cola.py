while(True):
    try:
        n = int(input())
        s = n
        while(n >= 3):
            s += int(n/3)
            n = int(n/3) + (n % 3)
        if(n == 2):
            s += 1
        print(s)
    except EOFError:
        break
