S = input() + "2"

count_1 = 0
count_0 = 0

for i in range(len(S) - 1) :
    if S[i] == "1" :
        if S[i+1] == "1":
            continue
        else :
            count_1 += 1

for i in range(len(S) - 1) :
    if S[i] == "0" :
        if S[i+1] == "0":
            continue
        else :
            count_0 += 1

if count_0 >= count_1 :
    print(count_1)
else :
    print(count_0)