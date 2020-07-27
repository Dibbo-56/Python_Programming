n = int(input())
for i in range(0, n):
    a, b = map(int, input().split())
    if(a == b):
        print("=")
    elif(a < b):
        print("<")
    elif(a > b):
        print(">")
