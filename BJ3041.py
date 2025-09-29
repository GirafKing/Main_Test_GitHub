dict = {
    # 1행 (Row 1)
    "A": (1, 1), 'B': (1, 2), 'C': (1, 3), 'D': (1, 4),
    
    # 2행 (Row 2)
    'E': (2, 1), 'F': (2, 2), 'G': (2, 3), 'H': (2, 4),
    
    # 3행 (Row 3)
    'I': (3, 1), 'J': (3, 2), 'K': (3, 3), 'L': (3, 4),
    
    # 4행 (Row 4)
    'M': (4, 1), 'N': (4, 2), 'O': (4, 3)
}

dict_input = {}
for i in range(1, 5) :
    A = list(input())
    for j in range(1, 5) :
        dict_input[A[j-1]] = (i, j)

result = 0
for i in dict :
    if i == "." :
        continue
    else :
        if dict[i] == dict_input[i] :
            continue
        else :
            for j in range(2) :
                a = dict[i]
                b = dict_input[i]
                result += abs(a[j] - b[j])

print(result)