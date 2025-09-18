N, M = map(int, input().split())
count = 0
result = 0
boolean = True
boolean_2 = False
start = -1
end = 0

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

    elif line.count("#") == 2 :
        for j in range(len(line)) :
            if line[j] == "#" :
                if start == -1 :
                    start = j
                else :
                    end = j

    elif line.count("#") == 1 :
        if line.index("#") == start :
            result = "RIGHT"
        elif line.index("#") == end :
            result = "LEFT"

    else :
        continue

print(result)