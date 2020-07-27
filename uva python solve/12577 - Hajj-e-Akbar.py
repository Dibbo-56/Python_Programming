i = 1
while True:
    str = input()
    if(str == "*"):
        break
    elif(str == "Hajj"):
        print("Case %d: Hajj-e-Akbar" % i)
    elif(str == "Umrah"):
        print("Case %d: Hajj-e-Asghar" % i)
    i += 1
