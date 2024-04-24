n = int(input())
gr = [[] for i in range(n + 1)]
root = 0
for i in range(1,n + 1):
    e = int(input())
    if e == 0:
        root = i
    else:
        gr[e].append(i)
        gr[i].append(e)
visited = [-1 for i in range(n + 1)]
visited[0] = 1
def dfs(v: int, p : int)-> None:
    visited[v] = (visited[p] + 1)%2
    for i in gr[v]:
        if visited[i] == -1:
            dfs(i, v)
dfs(root, 0)
print(visited)
print(max(visited.count(1) - 1, visited.count(0)))

