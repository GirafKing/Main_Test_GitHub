N = int(input())

L = set()
result = 0
for i in range(N) :
    a = input()

    if a == "ENTER" :
        result += len(L)
        L = set()
    else :
        L.add(a)

print(len(L) + result)