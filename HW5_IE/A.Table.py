from collections import deque

f = open('input.txt')
n, m = [int(x) for x in f.readline().split()]

dp = []

for line in f.readlines():
    dp.append([int(x) for x in line.split()])

q = deque()

for i in range(n):
    for j in range(m):
        if dp[i][j] == 1:
            q.append([i, j])

steps = [[0, 1], [0, -1], [1, 0], [-1, 0]]
while q:
    i, j = q.popleft()
    for di, dj in steps:
        if 0 <= i + di < n and 0 <= j + dj < m:
            if dp[i + di][j + dj] == 0:
                dp[i + di][j + dj] = dp[i][j] + 1
                q.append([i + di, j + dj])

for line in dp:
    print(*[x - 1 for x in line])
