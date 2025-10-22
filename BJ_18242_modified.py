N, M = map(int, input().split())
count = 0
result = 0
boolean = True
start = -1
end = 0

for i in range(N):
    line = list(input())
    hash_count = line.count("#")
    
    if hash_count >= 3 and boolean:
        count = hash_count
        boolean = False
    
    elif hash_count >= 3 and boolean == False:
        if count < hash_count:
            result = "UP"
        elif count > hash_count:
            result = "DOWN"
        else:
            continue
    
    elif hash_count == 2:
        for j in range(len(line)):
            if line[j] == "#":
                if start == -1:
                    start = j
                else:
                    end = j
    
    elif hash_count == 1:
        if line.index("#") == start:
            result = "RIGHT"
        elif line.index("#") == end:
            result = "LEFT"
    
    else:
        continue

print(result)