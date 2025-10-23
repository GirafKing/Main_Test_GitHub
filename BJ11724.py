N, M = map(int, input().split())

graph = {}
for _ in range(M) :
    a, b = map(int, input().split())

    if a not in graph:
        graph[a] = []
    graph[a].append(b)

    if b not in graph:
        graph[b] = []
    graph[b].append(a)

print(graph)