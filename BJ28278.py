out = []
stack = []

N = int(input())

for _ in range(N) :
    cmd = input().split()

    if cmd[0] == '1' :
        x = int(cmd[1])
        stack.append(x)

    elif cmd[0] == '2' :
        if stack :
            out.append(str(stack.pop()))
        else :
            out.append('-1')
    
    elif cmd[0] == '3' :
        out.append(str(len(stack)))

    elif cmd[0] == '4' :
        out.append('1' if not stack else '0')

    elif cmd[0] == '5' :
        if stack :
            out.append(str(stack[-1]))
        else :
            out.append('-1')

print('\n'.join(out))