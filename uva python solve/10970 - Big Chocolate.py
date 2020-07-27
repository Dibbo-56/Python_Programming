while (True):
    try:
        r, c = map(int, input().split())
        print((r-1) + r * (c-1))
    except EOFError:
        break
