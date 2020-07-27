while(True):
    a, b = map(int, input().split())
    if(a == -1 and b == -1):
        break
    elif(((a >= 0 and a <= 49) and (b >= 0 and b <= 49)) or
         ((a >= 50 and a <= 99) and (b >= 50 and b <= 99))):
        print(abs(a-b))
    elif(((a >= 0 and a <= 49) or (b >= 50 and b <= 99)) or
         ((b >= 0 and b <= 49) and (a >= 50 and a <= 99))):
        if(abs(a-b) <= 50):
            print(abs(a-b))
        else:
            if((a >= 0 and a <= 49) and (b >= 50 and b <= 99)):
                z = (a+1) + (99-b)
                print(z)
            else:
                z = (b+1) + (99-a)
                print(z)
