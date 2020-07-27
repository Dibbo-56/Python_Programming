while True:
    s = input()
    for i in range(len(s)):
        d = ord(s[i]) - 7
        print(chr(d),end="")
    print()
