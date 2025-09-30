#4659
while True :
    password = input()

    if password == "end" :
        break
    else :
        boolean = True
        vowels = {'a', 'e', 'i', 'o', 'u'}
        has_vowel = any(i in vowels for i in password)

        if not has_vowel :
            boolean = False
        else :
            vowel_count = 0
            consonant_count = 0
            
            for j in password :
                if j in vowels :
                    vowel_count += 1
                    consonant_count = 0
                else :
                    consonant_count += 1
                    vowel_count = 0
                
                if consonant_count >= 3 or vowel_count >= 3 :
                    boolean = False
                    break
            
            for k in range(len(password) - 1) :
                if password[k] == password[k+1] :
                    if password[k] == "e" or password[k] == "o" :
                        continue
                    else :
                        boolean = False
                        break
        
        if boolean :
            print(f"<{password}> is acceptable.")
        else :
            print(f"<{password}> is not acceptable.")