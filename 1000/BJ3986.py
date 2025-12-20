N = int(input())

count = 0
for _ in range(N) :
    stack = []
    word = input()

    for i in word :
        if stack :
            if stack[-1] == i :
                stack.pop()
            else :
                stack.append(i)
        else :
            stack.append(i)
        
    if not stack :
        count += 1

print(count)