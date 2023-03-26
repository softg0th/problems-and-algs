def dfs(graf, vis, now):
    if len(graf) == 1:
        return graf[now]
    for neig in graf[now]:
            if neig not in vis:
                print(neig)
                vis.append(neig)
                dfs(graf, vis, neig)
    return vis


n, m = map(int, input().split())

gr = []

for i in range(m):
    x, y = map(int, input().split())
    gr.append([x, y])

graph = []
for i in gr:
    graph.append(list(set(i)))

visited = []
sos = dfs(graph, visited, 0)
if len(sos) < 2:
    print(len(sos))
    print(sos)
else:
    print(len(sos))
    print(sorted(sos))
