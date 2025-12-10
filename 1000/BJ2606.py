#2606
T = int(input())
pair = int(input())
count = 0

graph = {}
for _ in range(pair):
    a, b = map(int, input().split())

    if a not in graph:
        graph[a] = []
    graph[a].append(b)

    if b not in graph:
        graph[b] = []
    graph[b].append(a)

if graph.get(1) :
    find = graph[1]
    L = [1]
    n = []

    while True :
        for i in find :
            if i in L :
                pass
            else :
                if i in graph :
                    L.append(i)
                    count += 1
                    n.extend(graph[i])
                else :
                    pass

        if len(n) == 0 :
            break
        else :
            find = n
            n = []

print(count)