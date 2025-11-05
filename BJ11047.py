N, K = map(int, input().split())
count = 0
L = []

for _ in range(N) :
    a = int(input())
    if a <= K :
        L.append(a)

count += K // L[-1]
K = K % L[-1]

l = []
while K > 0 :
    for i in L :
        if i <= K :
            l.append(i)
        
    count += K // l[-1]
    K = K % l[-1]

    L = l
    l = []

print(count)