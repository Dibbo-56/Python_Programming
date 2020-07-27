n=1
while(True):
    t=int(input())
    if(t==0):
        break

    arr=list(map(int,input().split()))

    sum,move=0,0
    for i in arr:
        sum += i

    avg=int(sum/t)
    for i in arr:
        if(avg<i):
            move += i-avg

    print("Set #%d" %n)
    print("The minimum number of moves is %d.\n" %move)
    n+=1
