from collections import deque

N = int(input())
papers = list(map(int, input().split()))
out = []

dq = deque()
for i in range(N) :
    dq.append((i+1, papers[i]))

for _ in range(N) :
    num, paper = dq.popleft()
    out.append(str(num))
    if paper > 0 :      
        dq.rotate(-(paper - 1))
    else :
        dq.rotate(-paper)

print(' '.join(out))