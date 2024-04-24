def binSearch(key, a):
    left = -1
    right = len(a)
    while left + 1 < right:  # while mid exists
        mid = (left + right) // 2
        # print(mid)
        if (a[mid] < key):
            left = mid
        elif a[mid] > key:
            right = mid
        else:
            return True
    return False


n, k = map(int, input().split())

a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]

for key in b:
    bool = binSearch(key, a)
    if bool:
        print("YES")
    else:
        print("NO")
