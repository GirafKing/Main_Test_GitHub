N = int(input())

L = list(map(int, input().split()))
result = -1

for i in range(51) :
    if L.count(i) == i :
        if result < i :
            result = i

print(result)