from collections import deque

s, t  = map(int, input().split())

q = deque()
L = ["+", "*", "-", "/"]

for i in L :
    q.append(i)
    a = s
    while True :
        