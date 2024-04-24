





from collections import deque

n, wSize = map(int, input().split())
arr = [int(x) for x in input().split()]

dq = deque()
for x in range(wSize):
    dq.append(arr[x])
# dq.append(arr[:wSize])
curMin = min(arr[:wSize])
print(curMin)
for i in range(wSize, n):
    el = dq.popleft()
    # print(el, "this is el")
    dq.append(arr[i])
    # print(dq)
    if arr[i] < curMin:
        curMin = arr[i]
        print(curMin)
    elif el == curMin:
        curMin = min(dq)
        print(curMin)
    else:
        print(curMin)
        # print(curMin, "LAMBDA")


# print(*dq)
# dq.pop()
# print(*dq)
