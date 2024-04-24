import sys
sys.setrecursionlimit(10**6)
n, m = map(int, input().split())
gr = [[] for i in range(n + 1)]
for i in range(m):
    u, v = map(int, input().split())
    gr[u].append(v)
    gr[v].append(u)

# print(gr)
points = set()
visited = [0 for i in range(n + 1)]
time = 0
tret =[0 for i in range(n + 1)]
tin =[0 for i in range(n + 1)]
def dfs(v : int, p : int) -> None:
    global visited, time, tin, tret, gr
    visited[v] = 1
    time += 1
    tin[v] = tret[v] = time
    cnt = 0
    for to in gr[v]:
        if to == p:
            continue
        if visited[to] == 0:
            dfs(to, v)
            cnt += 1
            tret[v] = min(tret[v], tret[to])
            if tin[v] <= tret[to] and p != -1:
                points.add(v)
        else:
            tret[v] = min(tret[v], tin[to])
    if p == -1 and cnt > 1:
        points.add(v)

for i in range(1, n + 1):
    dfs(i, -1)
print(len(points))
print(*sorted(points), sep='\n')