from collections import deque

N = int(input())
numbers = list(map(int, input().split()))
List = list(map(int, input().split()))

dq = deque()
for i in range(N) :
    if numbers[i] == 0 :      
        dq.append(List[i])


M = int(input())
put = list(map(int, input().split()))

out = []

for x in put :
    dq.appendleft(x)
    out.append(dq.pop())

print(" ".join(map(str, out)))