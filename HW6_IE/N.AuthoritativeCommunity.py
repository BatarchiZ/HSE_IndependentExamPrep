n, m = map(int, input().split())
rating = [0] + []
for i in range(n):
    rating.append(int(input()))

gr = [[] for i in range(n + 1)]
for i in range(m):
    u, v = map(int, input().split())
    gr[u].append(v)

print(gr)
print(rating)
visited = [0 for i in range(n + 1)]

path = []


def dfs(v: int) -> None:
    global visited, path
    visited[v] = 1
    for to in gr[v]:
        if visited[to] == 0:
            dfs(to)
    path.append(v)


dfs(6)
path = path[::-1]
print(path)
