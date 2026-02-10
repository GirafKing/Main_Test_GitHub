N, M = map(int, input().split())
j = int(input())

result = 0
for _ in range(j) :
    position = int(input())
    if M == 1 :
        result += abs(M - position)
    else :
        result += abs(M - position - (M-1))
print(result)