n = int(input())

numbers = []
for _ in range(n) :
    num = int(input())
    numbers.append(num)

cur = 1
stack = []
for x in numbers : 
    while cur <= x :
        stack.append(cur)
        cur += 1
        print("+")
    
    if stack[-1] == x :
        stack.pop()
        print("-")
    else :
        print("NO")
        break