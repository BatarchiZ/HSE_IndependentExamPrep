n, m = map(int, input().split())
gr = [[] for i in range(n + 1)]
for i in range(m):
    u, v = map(int, input().split())
    gr[u].append(v)
    gr[v].append(u)


cycle = 0
def dfs(v: int, p : int) -> None:
    global visited, cycle
    visited[v] = 2
    for i in gr[v]:
        if visited[i] == 0:
            dfs(i, v)
        elif visited[i] == 2 and i != p:
            cycle = 1
    visited[v] = 1

visited = [0 for i in range(n + 1)]
visited[0] = 1
dfs(1, -1)
# print(visited)
if sum(visited) == len(visited) and cycle == 0:
    print("YES")
else:
    print("NO")
# 4 4
# 1 2
# 1 3
# 2 3
# 1 4