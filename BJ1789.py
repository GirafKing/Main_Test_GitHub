#1789
S = int(input())
answer = 0

i = 0
while True :
    sum = (i * (i + 1)) / 2
    if sum > S :
        answer = i - 1
        break
    else :
        i += 1

print(answer)