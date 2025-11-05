N, K = map(int, input().split())
count = 0
L = []

for _ in range(N) :
    a = int(input())
    if a <= K :
        L.append(a)       

L.sort(reverse=True)

for i in L :
    count += K // i
    K %= i

print(count)