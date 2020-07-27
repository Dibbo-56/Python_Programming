t = int(input())
for i in range(0, t):
    n = int(input())
    ans = int((((((n*567) / 9) + 7492) * 235) / 47) - 498)
    ans = int(ans/10)
    ans = int(abs(ans) % 10)
    print(ans)
