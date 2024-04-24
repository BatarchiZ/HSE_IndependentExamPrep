n, m = map(int, input().split())
gr = [[] for i in range(n + 1)]
for i in range(m):
    u, v = map(int,input().split())
    gr[u].append(v)
    gr[v].append(u)

# print(gr)
colours = [-1 for i in range(n + 1)]
colours[0] = 1
checker = 1
def dfs(v : int, p):
    global colours, checker
    colours[v] = colours[p]%2 + 1
    for i in gr[v]:
        if colours[i] == -1:
            dfs(i, v)
        elif colours[i] == colours[v]:
            checker = 0
for i in range(1, n + 1):
    if colours[i] == -1:
        dfs(i, 0)
# print(colours)
if checker == 1:
    print("YES")
else:
    print("NO")