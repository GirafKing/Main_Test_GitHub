import sys
input = sys.stdin.readline

N = int(input())

windows = [0 for i in range(1, N+1)]
print(windows)

for i in range(1, N+1) :
    for j in range(1, N+1) :
        if (j % i) == 0 :
            if windows[j-1] == 0 :
                windows[j-1] = 1
            else :
                windows[j-1] = 0
    print(windows)

print(windows.count(1))