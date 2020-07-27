t = int(input())

for i in range(1, t+1):
    n = int(input())
    a = n
    while True:
        sum = 0
        while a != 0:
            d = a % 10
            sum += d*d
            a = a//10
        if sum == 1:
            print("Case #%d: %d is a Happy number." % (i, n))
            break
        if sum == n:
            print("Case #%d: %d is an Unhappy number." % (i, n))
            break
        if sum <= 4:
            print("Case #%d: %d is an Unhappy number." % (i, n))
            break

        a = sum
