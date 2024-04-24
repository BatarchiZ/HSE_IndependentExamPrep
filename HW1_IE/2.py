import math
def binSearch(key):
    left = 0.0
    right = 2**64.0
    while left + 0.00001 < right:
        mid = (left + right)/2
        # print(mid)
        square = mid**2
        if(square <= key):
            left = mid
        elif(square > key):
            right = mid
        # if(square == key):
        #     return int(mid)
    return math.floor(left)
# a = [x for x in range(2**32)]
# n = input()
print(binSearch(999999))
