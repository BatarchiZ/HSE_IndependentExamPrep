import math


def binSearch(key):
    left = -1
    right = 2 ** 256
    while left + 1 < right:
        mid = (left + right) // 2
        # print(mid)
        prevSquare = (mid - 1) ** 2
        square = mid ** 2
        nextSquare = (mid + 1) ** 2
        if (square < key):
            left = mid
        elif (square > key):
            right = mid
        elif square == key:
            return mid
        if (square < key and nextSquare > key):
            return math.floor(mid)
        if (square > key and prevSquare < key):
            return math.floor(mid) - 1
    # return math.floor(left)


f = open("input.txt")
for n in f.readlines():
    n = int(n)
    print(binSearch(n))
