while (True):
    str = input()
    if(str == "DONE"):
        break
    s = ""
    for i in range(len(str)):
        if((str[i] >= 'a' and str[i] <= 'z') or
           (str[i] >= 'A' and str[i] <= 'Z')):
            s += str[i]
    s = s.lower()
    rev = s[::-1]
    if(s == rev):
        print("You won't be eaten!")
    else:
        print("Uh oh..")
