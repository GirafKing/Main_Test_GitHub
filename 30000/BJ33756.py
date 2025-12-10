def eight(n) :
    if n == 0 :
        return False
    while n > 0 :
        if n != 0 :
            return False
        n //= 8
    return True

T = int(input())
for _ in range(T) :
    n = int(input())
    if eight(n) :
        print("Yes")
    else :
        print("No")