def binL(key: int, a: list) -> int:
    left = -1
    right = len(a)
    while right > left + 1:
        mid = (left + right) // 2
        if a[mid] < key:
            left = mid
        else:
            right = mid
    if right != len(a) and a[right] == key:
        return right
    else:
        return left + 1

def binR(key: int, a: list) -> int:
    left = -1
    right = len(a)
    while right > left + 1:
        mid = (left + right) // 2
        if a[mid] <= key:
            left = mid
        else:
            right = mid
    if left != -1 and a[left] == key:
        return left
    else:
        return right - 1


n = int(input())
a = [int(x) for x in input().split()]
a.sort()
# print(a)
c = int(input())
for i in range(c):
    k1, k2 = map(int, input().split())
    li = binL(k1, a)
    ri = binR(k2, a)
    # print(li)
    # print(ri)
    print(ri - li + 1, end=' ')
    # print()
# 5
# 1 2 2 4 5
# 4
# 1 5
# 2 4
# 3 3
# 3 5
