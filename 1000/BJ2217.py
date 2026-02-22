N = int(input())

find = []
for _ in range(N) :
    loap = int(input())
    find.append(loap)

find = sorted(find)

count = N
result = []

for i in find :
    if count == 0 :
        weight = i
    else :
        weight = i * count
    result.append(weight)
    count -= 1

print(max(result))