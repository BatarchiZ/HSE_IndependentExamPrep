






n, w = map(int, input().split())
arr = [int(x) for x in input().split()]

minArr = [2**32 for i in range(n - w + 1)]
for i in range(n - w + 1):
    minArr[i] = min(arr[i:i + w])
    # for j in range(w):
    #     minArr[i] = min(minArr[i], arr[i + j])
    # minArr[i] = min(arr[i], arr[i + 1], arr[i + 2])

print(*minArr, sep = '\n')