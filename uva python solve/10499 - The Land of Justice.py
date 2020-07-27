while True:
    n = int(input())
    if n < 0:
        break
    if n == 1:
        print('0%')
        continue
    profit = 25*n
    print('%d%%' % profit)
