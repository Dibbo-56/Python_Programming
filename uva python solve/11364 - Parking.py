t = int(input())
for i in range(0, t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    sum = 0
    for i in range(0, n-1):
        sum += abs(arr[i] - arr[i+1])
    print(2*sum)
