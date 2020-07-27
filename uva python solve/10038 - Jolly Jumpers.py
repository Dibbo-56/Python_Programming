while(True):
    arr, dif, f = [], [], 1
    try:
        arr = list(map(int, input().split()))
        n = arr[0]
        for i in range(1, arr[0]):
            dif.append(abs(arr[i] - arr[i+1]))
        dif.sort()
        for i in range(0, n-1):
            if(dif[i] == i+1):
                f = 1
            else:
                f = 0
                break
        if(f == 1):
            print("Jolly")
        else:
            print("Not jolly")
    except EOFError:
        break
