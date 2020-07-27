t = int(input())

for i in range(t):
    n = int(input())
    digit = {}

    for j in range(10):
        digit[j] = 0

    for j in range(1, n+1):
        d = j
        while(d != 0):
            m = d % 10
            digit[m] = digit[m] + 1
            d = d//10

    print('%d %d %d %d %d %d %d %d %d %d' % (digit[0], digit[1], digit[2],
                                             digit[3], digit[4], digit[5],
                                             digit[6], digit[7], digit[8],
                                             digit[9]))
