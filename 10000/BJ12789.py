N = int(input())
line = list(map(int, input().split()))

now = 1
stack = []

for x in line :
    while stack and stack[-1] == now :
        stack.pop()
        now += 1

    if x == now :
        now += 1
    else :
        stack.append(x)

while stack and stack[-1] == now :
    stack.pop()
    now += 1

if now - 1 == N :
    print("Nice")
else :
    print("Sad")