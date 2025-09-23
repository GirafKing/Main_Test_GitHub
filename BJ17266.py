#17266
N = int(input()) # 굴다리 길이
M = int(input()) # 가로등의 개수
x = list(map(int, input().split())) # 가로등의 위치

M = max(x[0], N - x[-1])
for i in range(len(x) - 1) :
    a = (x[i+1] - x[i] + 1) // 2
    if a > M :
        M = a

print(M)