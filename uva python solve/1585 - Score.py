t = int(input())
for i in range(1, t+1):
    s = input()
    c, sum = 1, 0
    for j in range(len(s)):
        if s[j] == 'O':
            sum += c
            c += 1
        elif s[j] == 'X':
            c = 1
    print("%d" % sum)
