t = int(input())
for i in range(1, t+1):
    a, b, c = map(int, input().split())
    if(a+b > c and a+c > b and b+c > a):
        print("OK")
    else:
        print("Wrong!!")
