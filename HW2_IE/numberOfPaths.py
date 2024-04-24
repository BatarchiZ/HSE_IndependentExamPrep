



n, m = map(int, input().split())
matrix = [[0 for x in range(n)] for y in range(m)]
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if i == j == 0:
            matrix[i][j] = 1
        elif i == 0 or j == 0:
            matrix[i][j] = 1
        else:
            matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1]


# print(*matrix, sep= '\n')
print(matrix[-1][-1])
