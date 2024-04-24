






# import random
# rd = random
n = int(input())
a = [0] + [int(x) for x in input().split()]
p = [0 for i in range(len(a))]
minn = [0 for i in range(len(a))]
index_minn = [0 for i in range(len(a))]

max_sum = a[1]
index_ans = 1

for i in range(1, len(a)):
    p[i] = p[i - 1] + a[i]
    minn[i] = minn[i - 1]
    index_minn[i] = index_minn[i - 1]
    if p[i - 1] < minn[i - 1]:
        minn[i] = p[i - 1]
        index_minn[i] = i - 1
    if p[i] - minn[i] > max_sum:
        max_sum = p[i] - minn[i]
        index_ans = i

print(index_minn[index_ans] + 1, index_ans, max_sum)
# print(*a)
# print(*p)
# print(*minn)
# print(*index_minn)
# print(max_sum)
# print(f'L = {index_minn[index_ans] + 1} R = {index_ans}')