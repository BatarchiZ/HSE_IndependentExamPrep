from collections import deque

f = open('input.txt')
n, m = map(int, f.readline().split())
matrix = []

for i in range(n):
    line = f.readline()
    arr = [-int(x) for x in line.split()]
    # print(arr)
    matrix.append(arr)

x1, y1 = map(int, f.readline().split())
x2, y2 = map(int, f.readline().split())
x1 -= 1
y1 -= 1
x2 -= 1
y2 -= 1
matrix[y1][x1] = 1
# print(*matrix, sep='\n')
# print()
q = deque()
q.append([y1, x1])

delta = [[0, 1], [0, -1], [1, 0], [-1, 0]]
while q:
    i, j = q.popleft()
    # print(i, j)
    for di, dj in delta:
        if (0 <= i + di < n and 0 <= j + dj < m) and matrix[i + di][j + dj] == 0:
            q.append([i + di, j + dj])
            matrix[i + di][j + dj] = matrix[i][j] + 1

    # for line in matrix:
    #     print(*line, sep = '\t')
    # print(*matrix, sep='\n')
    # print()

if(matrix[y2][x2] > 0):
    print(matrix[y2][x2] - 1)
else:
    print(-1)

