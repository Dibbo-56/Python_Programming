n = int(input())
arr = []
for i in range(0, n):
    arr = list(map(int, input().split()))
    arr.sort()
    print("Case %d: %d" % (i+1, arr[1]))
    arr.clear()
