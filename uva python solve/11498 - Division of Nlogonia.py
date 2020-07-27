while True:
    t = int(input())
    if(t == 0):
        break
    n, m = map(int, input().split())
    for i in range(0, t):
        x, y = map(int, input().split())
        if(x == n or y == m):
            print("divisa")
        elif(x < n and y > m):
            print("NO")
        elif(x > n and y > m):
            print("NE")
        elif(x < n and y < m):
            print("SO")
        else:
            print("SE")
