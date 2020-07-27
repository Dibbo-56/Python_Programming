arr = [0, 1]
for i in range(2, 101):
    arr.append((i*i) + arr[i-1])
while (True):
    n = int(input())
    if(n == 0):
        break
    print(arr[n])
