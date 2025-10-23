n = int(input())
m = int(input())

grape = {}
for _ in range(m) :
    a, b = map(int, input().split())

    if a not in grape :
        grape[a] = []
    grape[a].append(b)

    if b not in grape :
        grape[b] = []
    grape[b].append(a)

if grape.get(1) :
    friends = []
    for i in grape[1] :
        a = grape[i]
        friends.extend(a)

    friends.append(grape[1])

    result = set(friends)

    if 1 in result :
        print(len(result) - 1)
    else :
        print(len(result))

else :
    print(0)