import sys
input = sys.stdin.readline

N = int(input())

numbers = list(map(int, input().split()))
out = []

S = sorted(set(numbers))
pos = {}
for i, v in enumerate(S) :
    pos[v] = i

for num in numbers :
    a = str(pos[num])
    out.append(a)

print(" ".join(out))