import sys
sys.setrecursionlimit(10**6)
n, m = map(int, input().split())
gr = [[] for i in range(n + 1)]
for i in range(m):
    u, v = map(int, input().split())
    gr[u].append(v)

# print(gr)

visited = [0 for i in range(n + 1)]
visited[0] = 1
path = []
cycle = 0
def dfs(v : int, p : int):
    global visited, cycle, path
    visited[v] = 2
    for i in gr[v]:
        if visited[i] == 2:
            cycle = 1
        elif visited[i] == 0:
            dfs(i, v)
    visited[v] = 1
    path.append(v)

for i in range(1, len(gr)):
    if visited[i] == 0:
        dfs(i, -1)
if cycle == 0:
    print(*path[::-1], '\n')
else:
    print(-1)