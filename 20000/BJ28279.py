from collections import deque
import sys

input = sys.stdin.readline
dq = deque()
out = []
N = int(input())

for _ in range(N) :
    cmd = input().split()
    if cmd[0] == "1" :
        cmd[1] = int(cmd[1])
        dq.appendleft(cmd[1])

    elif cmd[0] == "2" :
        cmd[1] = int(cmd[1])
        dq.append(cmd[1])

    elif cmd[0] == "3" :
        if dq :
            a = dq.popleft()
            out.append(a)
        else :
            out.append(-1)

    elif cmd[0] == "4" :
        if dq :
            a = dq.pop()
            out.append(a)
        else :
            out.append(-1)

    elif cmd[0] == "5" :
        out.append(len(dq))
    
    elif cmd[0] == "6" :
        if not dq :
            out.append(1)
        else :
            out.append(0)
    
    elif cmd[0] == "7" :
        if dq :
            out.append(dq[0])
        else :
            out.append(-1)

    elif cmd[0] == "8" :
        if dq :
            out.append(dq[-1])
        else :
            out.append(-1)

for i in out :
    print(i)