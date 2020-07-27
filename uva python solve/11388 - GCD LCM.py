t = int(input())

for i in range(t):
    a, b = map(int, input().split())
    if b % a == 0:
        print('%d %d' % (a, b))
    else:
        print('-1')
