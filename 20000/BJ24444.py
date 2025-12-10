from collections import deque
import sys

input = sys.stdin.readline
N, M, R = map(int, input().split())

g = {}
for _ in range(M):
    u, v = map(int, input().split())
    g.setdefault(u, []).append(v)
    g.setdefault(v, []).append(u)

for i in range(1, N+1):
    g.setdefault(i, [])
    g[i].sort()

visited_order = [0] * (N + 1)
order = 1

def bfs(start):
    global order
    q = deque([start])
    visited_order[start] = order

    while q:
        cur = q.popleft()
        for nxt in g[cur]:
            if visited_order[nxt] == 0:
                order += 1
                visited_order[nxt] = order
                q.append(nxt)

bfs(R)
print("\n".join(str(visited_order[i]) for i in range(1, N+1)))
