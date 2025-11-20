N = int(input())
stack = []
for _ in range(N) :
    cmd = input().split()
    if cmd[0] == '1' :
        x = int(cmd[1])
        stack.append(x)

    elif cmd[0] == '2' :
        if stack :
            print(stack[0])
        else :
            print(-1)
    
    elif cmd[0] == '3' :
        print(len(stack))

    elif cmd[0] == '4' :
        if not stack :
            print(1)
        else :
            print(0)

    elif cmd[0] == '5' :
        if stack :
            print(stack[0])
        else :
            print(-1)