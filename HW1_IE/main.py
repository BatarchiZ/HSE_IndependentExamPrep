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


a = [1, 1,3, 3,9, 9]
print(binL(2, a))
print(binR(8, a))