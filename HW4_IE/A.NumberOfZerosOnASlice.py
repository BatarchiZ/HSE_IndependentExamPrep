



n = int(input())
arr = [-1] + [int(x) for x in input().split()]
parr = [0 for x in range(n + 1)]

for i in range(1, n + 1):
    if (arr[i] == 0):
        parr[i] = parr[i - 1] + 1
    else:
        parr[i] = parr[i - 1]
# print(arr)
# print(parr)
q = int(input())
for x in range(q):
    a, b = map(int, input().split())
    print(parr[b] - parr[a - 1], end=' ')