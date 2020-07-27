t = int(input())
arr = []
for i in range(1, t+1):
    n = int(input())
    arr = list(map(int, input().split()))
    mn = arr[0]
    high = 0
    low = 0
    for j in range(1, len(arr)):
        if(mn < arr[j]):
            high + =1
        if(mn > arr[j]):
            low += 1
        mn = arr[j]
    print("Case %d: %d %d" % (i, high, low))
    arr.clear()
