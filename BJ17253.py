def three(n) :
    if n == 0 :
        return False
    while n > 0 :
        if n % 3 == 2 :
            return False
        n //= 3
    return True

n = int(input())
print("YES" if three(n) else "NO")