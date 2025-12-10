#12981
L = sorted(map(int, input().split()))
box_count = 0

# one
t = L[0]
box_count += t
for i in range(3):
    L[i] -= t

# three
for j in range(3) :
    box_count += L[j] // 3
    L[j] %= 3

# last
if L[1] == 1 and L[2] == 1:
    box_count += 1
else :
    if L[1] > 0 : 
        box_count += 1
    if L[2] > 0 : 
        box_count += 1
        
print(box_count)