
from collections import deque

def convert(c : str):
    j = 0
    if c[0] == 'a':
        j = 0
    elif c[0] == 'b':
        j = 1
    elif c[0] == 'c':
        j = 2
    elif c[0] == 'd':
        j = 3
    elif c[0] == 'e':
        j = 4
    elif c[0] == 'f':
        j = 5
    elif c[0] == 'g':
        j = 6
    elif c[0] == 'h':
        j = 7
    elif c[0] == 'i':
        j = 8
    return int(c[1]) - 1, j

delta = [[-2, 1],[-2, -1], [2, 1], [2, -1],
         [1, 2], [1, -2], [-1, 2], [-1, -2]]

def dfs(i, j):
    matrix = [[0 for i in range(8)] for j in range(8)]
    q = deque()
    q.append([i,j])
    while q:
        i, j = q.popleft()
        for di, dj in delta:
            if 0 <= i + di < 8 and 0 <= j + dj < 8 and matrix[i + di][j + dj] == 0:
                matrix[i + di][j + dj] = matrix[i][j] + 1
                q.append([i+di, j+dj])
    return matrix


s1, s2 = input().strip().split()
i1, j1 = convert(s1)
i2, j2 = convert(s2)
# print(i1, j1)
# print(i2, j2)
matrix1 = dfs(i1, j1)
matrix2 = dfs(i2, j2)
minN = 2**32
for i in range(8):
    for j in range(8):
        if matrix1[i][j] == matrix2[i][j] and matrix1[i][j] < minN:
            minN = matrix1[i][j]

if minN == 2**32:
    print(-1)
else:
    print(minN)

# q = deque()
# q.append([i1, j1])
# while q:
#