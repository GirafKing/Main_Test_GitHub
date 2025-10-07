import sys
input = sys.stdin.readline

N, M = map(int, input().split())

array = []
for _ in range(N) :
    numbers = list(map(int, input().split()))
    array.append(numbers)

K = int(input())
for _ in range(K) :
    i, j, x, y = map(int, input().split())
    S = 0

    for I in range(i, x+1) :
        for J in range(j, y+1) :
            S += array[I-1][J-1]

    print(S)