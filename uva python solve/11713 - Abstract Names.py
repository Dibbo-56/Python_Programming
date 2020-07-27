t = int(input())

for i in range(t):
    s1 = input()
    s2 = input()

    if len(s1) == len(s2):
        flag = 1
        for j in range(len(s1)):
            if s1[j] == s2[j]:
                continue
            else:
                if (s1[j] == 'a' or s1[j] == 'e' or s1[j] == 'i' or
                    s1[j] == 'o' or s1[j] == 'u') and (s2[j] == 'u' or
                                                       s2[j] == 'e' or
                                                       s2[j] == 'i' or
                                                       s2[j] == 'o' or
                                                       s2[j] == 'a'):
                    continue
                else:
                    flag = 0

        if flag == 1:
            print("Yes")
        else:
            print("No")
    else:
        print("No")
