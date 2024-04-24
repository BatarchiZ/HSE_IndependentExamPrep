#
# n, w = map(int, input().split())
# arr = [int(x) for x in input().split()]
#
# minArr = [2**32 for i in range(n - w + 1)]
# for i in range(n - w + 1):
#     for j in range(w):
#         minArr[i] = min(minArr[i], arr[i + j])
#     # minArr[i] = min(arr[i], arr[i + 1], arr[i + 2])
#
# print(*minArr, sep = '\n')

import random

rd = random
n, w = map(int, input().split())

sz_blok = w - 1
a = [int(x) for x in input().split()]
# sz_blok = int(len(a) ** 0.5)

bloks = [2 ** 30 for i in range(len(a) // sz_blok + 1)]
for i in range(len(a)):
    bloks[i // sz_blok] = min(bloks[i // sz_blok], a[i])
# запрос
# print(*a)
print(bloks)
for k in range(n - 1):
    print(bloks[k//sz_blok])

# for k in range(0, n - w + 1):
#     minn = 2 ** 30
#     L = k
#     R = k + w - 1
#     i = L
#     while i <= R:
#         if i % sz_blok == 0 and i // sz_blok != R // sz_blok:
#             minn = min(minn, bloks[i // sz_blok])
#             i += sz_blok
#         else:
#             minn = min(minn, a[i])
#             i += 1
#     # print(*a)
#     print(minn)
# L = 3
# R = 4
# i = L

