t = int(input())
for i in range(0, t):
    arr = list(map(int, input().split()))
    arr = arr[0:4] + sorted(arr[4:])
    c = (arr[5] + arr[6]) / 2.0
    sum = arr[0] + arr[1] + arr[2] + arr[3] + c
    if(sum >= 90):
        print("Case %d: A" % (i+1))
    elif(sum < 90 and sum >= 80):
        print("Case %d: B" % (i+1))
    elif(sum < 80 and sum >= 70):
        print("Case %d: C" % (i+1))
    elif(sum < 70 and sum >= 60):
        print("Case %d: D" % (i+1))
    else:
        print("Case %d: F" % (i+1))
    arr.clear()
