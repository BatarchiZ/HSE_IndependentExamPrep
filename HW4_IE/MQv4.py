




from collections import deque
import random as rd


n, w = map(int, input().split())
arr = [int(x) for x in input().split()]
dq = deque()
for i in range(n):
    if(len(dq)!= 0 and i - dq[0][0] >= w ):
        dq.popleft()
    x = arr[i]
    while len(dq) != 0 and dq[-1][1] > x:
        dq.pop()
    dq.append([i,x])
    if i + 1 >= w:
        print(dq[0][1])
