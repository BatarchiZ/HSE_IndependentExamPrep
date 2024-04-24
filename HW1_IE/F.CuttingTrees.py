def binSearch(a, k, b, m, key):
    left = -1
    right = 2 ** 64
    while left + 1 < right:
        days = (left + right) // 2
        # print(days)
        dimaRestDay = days // k
        fedorRestDay = days // m
        trees = days * (a + b) - dimaRestDay * a - fedorRestDay * b
        if (trees >= key):
            right = days
        else :
            left = days
        # else:
        #     print(days)
        #     return
    print(right)


a, k, b, m, x = map(int, input().split())
binSearch(a, k, b, m, x)
