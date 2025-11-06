N = int(input())
L = list(map(int, input().split()))
score = 0

l = []
for i in L :
    if i == 1 :
        l.append(i)
        score += len(l)
    else :
        l = []

print(score)