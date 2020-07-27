t = int(input())
arr = []
for i in range(0, t):
    arr = list(map(int, input().split()))
    del arr[0]
    arr.sort(reverse=True)
    mn = arr[0]
    print("Case %d: %d" % (i+1, mn))
    arr.clear()
