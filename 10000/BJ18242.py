N, M = map(int, input().split())
count = 0
result = ""
start = -1
end = 0

for i in range(N) :
    line = list(input())

    if line.count("#") >= 3:

        if count == 0:
            count = line.count("#")

        elif count < line.count("#"):
            result = "UP"
            
        elif count > line.count("#"):
            result = "DOWN"

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