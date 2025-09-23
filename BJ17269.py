dict = {
    'A': 3,
    'B': 2,
    'C': 1,
    'D': 2,
    'E': 4,
    'F': 3,
    'G': 1,
    'H': 3,
    'I': 1,
    'J': 1,
    'K': 3,
    'L': 1,
    'M': 3,
    'N': 2,
    'O': 1,
    'P': 2,
    'Q': 2,
    'R': 2,
    'S': 1,
    'T': 2,
    'U': 1,
    'V': 1,
    'W': 1,
    'X': 2,
    'Y': 2,
    'Z': 1}

N, M = map(int, input().split())
name_1, name_2 = input().split()

# 초기 이름 만들기
target = ""
plus_name = ""

min_len = min(N, M)
for i in range(min_len) :
    target += name_1[i]
    target += name_2[i]

if N < M :
    plus_name = name_2[N:]
elif N > M :
    plus_name = name_1[M:]

target += plus_name

# 초기 상태 만들기
first = []
for j in target :
    a = dict[j]
    first.append(a)

L = []
while True :
    for i in range(len(first) - 1) :
        a = first[i] + first[i+1]
        if a < 10 :
            L.append(a)
        else :
            a = a % 10
            L.append(a)

    if len(L) == 2 :
        L[0], L[1] = str(L[0]), str(L[1])
        break
    else :
        first = L
        L = []

if L[0] == "0" :
    print(f"{L[1]}%")
else :
    print(f"{L[0]}{L[1]}%")