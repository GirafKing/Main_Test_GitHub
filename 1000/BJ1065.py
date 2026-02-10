N = int(input())

count = 0
n = 1

while n <= N :
    if len(str(n)) == 1 or len(str(n)) == 2 :
        count += 1
    else :
        S = str(n)
        a = int(S[0]) - int(S[1])
        B = True
        for i in range(len(S) - 1) :
            if int(S[i]) - int(S[i+1]) != a :
                B = False
                break

        if B :
            count += 1

    n += 1

print(count)