t = int(input())
arr = []
for i in range(0, t):
    arr = list(map(int, input().split()))
    n = arr[0]
    sum = 0
    for j in range(1, n+1):
        sum += arr[j]
    avg = sum/n
    cnt = 0
    for j in range(1, n+1):
        if (arr[j] > avg):
            cnt += 1
    print("%.3f%%" % ((cnt/n) * 100))
    arr.clear()
