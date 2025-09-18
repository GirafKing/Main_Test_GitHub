N, M = map(int, input().split())
count = 0
result = 0
boolean = True
boolean_2 = False

for i in range(N) :
    line = list(input())

    if line.count("#") >= 3 and boolean :
        count = line.count("#")
        boolean = False
    elif line.count("#") >= 3 and boolean == False :
        if count < line.count("#") :
            result = "UP"
            boolean_2 = True
        elif count > line.count("#") :
            result = "DOWN"
            boolean_2 = True
        else :
            continue

    elif line.count("#") >= 1 :
        if line.count("#") != 2 :
            line_left = line[:len(line) // 2]
            line_right = line[len(line) // 2:]
            if "#" in line_left :
                result = "RIGHT"
            else :
                result = "LEFT"
            
    else :
        continue

print(result)