s = input()

find = set(s)
count = 0
three = ''

for i in find :
    t = s.count(i)
    if (t%2) == 0 :
        pass
    else :
        three = i
        count += 1

if count >= 2 :
    print("I'm Sorry Hansoo")
else :
    forward = ''
    for i in find :
        forward += i * (s.count(i) // 2)
    
    forward = ''.join(sorted(forward))

    print(forward + three + forward[::-1])