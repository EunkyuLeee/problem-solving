def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=" ")
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, v, visited):
    q = [v]
    visited[v] = True
    while len(q) != 0:
        for i in graph[q[0]]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
        print(q.pop(0), end=" ")

n, m, v = map(int, input().split())

g = [[] for i in range(n + 1)]

for i in range(m):
    n1, n2 = map(int, input().split())
    g[n1].append(n2)
    g[n1].sort()
    g[n2].append(n1)
    g[n2].sort()

visited = [False] * (n + 1)

dfs(g, v, visited)
print()
visited = [False] * (n + 1)
bfs(g, v, visited)