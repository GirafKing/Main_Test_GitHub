from collections import deque

T = int(input())

for _ in range(T) :
    N, M = map(int, input().split())
    q = deque()
    result = 0

    A = list(map(int, input().split()))

    for j in range(len(A)) :
        if j != M :
            q.append((A[j], 0))
        else :
            q.append((A[j], 1))
            
    count = [0] * 10
    for i in A :
        count[i] += 1

    current_max = max(A)

    