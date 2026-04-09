N = int(input())
serials = []

for _ in range(N) :
    serial_number = input()
    serials.append(serial_number)

def get_sum(x) :
    total = 0
    for c in x :
        if c.isdigit() :
            total += int(c)
    return total    

serials.sort(key = lambda x : (len(x), get_sum(x), x))

for i in serials :
    print(i)