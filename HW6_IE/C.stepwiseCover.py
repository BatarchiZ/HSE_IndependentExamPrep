n, m, k = map(int, input().split())
gr = [[] for i in range(n + 1)]
for i in range(m):
    u, v = map(int, input().split())
    gr[u].append(v)
    gr[v].append(u)

ans = []
visited = [0 for i in range(n + 1)]
path = []

def dfs(v: int):
    global gr, visited, path, ans
    visited[v] = 1
    path.append(v)
    for i in gr[v]:
        if visited[i] == 0:
            dfs(i)
            path.append(v)
dfs(k)
ans = path
print(len(ans))
print(*ans, sep=' ', end= ' ')