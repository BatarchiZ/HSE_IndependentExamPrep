f = open('input.txt')
n, m = [int(x) for x in f.readline().split()]
gr = [[] for i in range(n)]

for line in f.readlines():
    u, v = [int(x) for x in line.split()]
    u -= 1
    v -= 1
    gr[u].append(v)
    gr[v].append(u)

used = [0 for i in range(n)]
st = []
st.append(0)  # начнём dfs с 0 вершины

while st:
    cur = st[-1]
    while gr[cur]:
        to = gr[cur].pop()
        if used[to] == 0:
            used[to] = 1
            st.append(to)
            break
    else:
        st.pop()
if sum(used) == n:
    print("YES")
else:
    print("NO")
