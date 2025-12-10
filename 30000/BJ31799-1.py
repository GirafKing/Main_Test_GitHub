import re

N = int(input())
scores = input()

score_list = re.findall(r'[A-C][+0-]?', scores)

for i in range(len(score_list)):
    if len(score_list[i]) == 1:
        score_list[i] = score_list[i] + "0"

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
            previous_term = score_list[j]
            term += 1

        elif previous_term in ["A+", "A0", "A-", "B+", "B0", "B-"] :
            result += "B"
            previous_term = score_list[j]
            term += 1


    elif score_list[j] in ["A-", "B+"] :
        if term == 1 or previous_term in ["B0", "B-", "C+", "C0", "C-"] :
            result += "P"
            previous_term = score_list[j]
            term += 1

        elif previous_term in ["A+", "A0", "A-", "B+"] :
            result += "D"
            previous_term = score_list[j]
            term += 1


    elif score_list[j] == "A0" :
        if term == 1 or previous_term in ["A-", "B+", "B0", "B-", "C+","C0", "C-"] :
            result += "E"
            previous_term = score_list[j]
            term += 1
        elif previous_term in ["A+", "A0"] :
            result += "P"
            previous_term = score_list[j]
            term += 1
    

    elif score_list[j] == "A+" :
        result += "E"
        previous_term = score_list[j]
        term +=1

print(result)