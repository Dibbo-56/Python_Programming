t = int(input())


def reverse(s):
    rev = s[::-1]
    return rev

for i in range(0, t):
    num1 = int(input())
    cnt = 0
    while(True):
        num2 = int(reverse(str(num1)))
        num = num1 + num2
        str1 = str(num)
        str2 = reverse(str(num))
        cnt += 1
        if(str1 == str2):
            break
        num1 = num
    print("%d %d" % (cnt, num))
