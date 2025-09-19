#31799
N = int(input())
scores = input()
score_list = []

for i in scores :
    if i.isalpha() :
        grade = i
    else :
        grade = grade + i
        score_list.append(grade)

for s in scores:
    if len(s) == 1 :
        s = s + "0" 
    score_list.append(s)

result = ""
previous_term = ""
term = 1

for j in range(len(score_list)) :
    if score_list[j] in ["C+", "C0", "C-"] :
        result += "B"
        previous_term = score_list[j]
        term += 1

    elif score_list[j] in ["B0", "B-"] :
        if term == 1 or previous_term in ["C+", "C0", "C-"] :
            result += "D"
            term += 1

    elif previous_term in ["A+", "A0", "A-", "B+", "B0", "B-"] :
        result += "B"
        term += 1

    elif score_list[j] in ["A-", "B+"] :
            
        if term == 1 or previous_term in ["B0", "B-", "C+", "C0", "C-"] :
            result += "P"
            term += 1

        elif previous_term in ["A", "A0", "A-", "B+"] :
            result += "D"
            term += 1

    elif score_list[j] == "A0" :

        if term == 1 or previous_term in ["A-", "B+", "B0", "B-", "C+","C0", "C-"] :
            result += "P"
            term += 1
    
    elif score_list[j] == "A+" :
        result += "E"

print(result)