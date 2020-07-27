prime = {1: 1}
for i in range(2, 1050):
    isprime = True
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            isprime = False
            break
    if (isprime):
        prime.update({i: 1})
    else:
        prime.update({i: 0})

while (True):
    try:
        str = input()
        sum = 0
        for i in range(len(str)):
            if (str[i] >= 'a' and str[i] <= 'z'):
                sum += ord(str[i]) - 96
            else:
                sum += ord(str[i]) - 38

        if (prime[sum] == 1):
            print("It is a prime word.")
        else:
            print("It is not a prime word.")

    except EOFError:
        break
