N, L = map(int, input().split())
fruits_height = list(map(int, input().split()))
fruits_height.sort()

for i in range(N) :
    if fruits_height[i] <= L :
        L += 1

print(L)