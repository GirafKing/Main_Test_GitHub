
N, M, V = map(int, input().split())

g = {}
for _ in range(M) :
    a, b = map(int, input().split())
    g.setdefault(a, []).append(b)
    g.setdefault(b, []).append(a)

