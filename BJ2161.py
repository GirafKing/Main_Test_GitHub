from collections import deque

N = int(input())
q = deque()
l1 = []

for i in range(1, N+1) :
    q.append(i)

for j in range(N - 1) :
    a = q.popleft()
    l1.append(a)
    b = q.popleft()
    q.append(b)

c = q.pop()
l1.append(c)
print(*l1)