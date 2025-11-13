while True :
    stack = []
    boolean = True
    String = input()
    if String == "." :
        break

    else :
        for ch in String:
            if ch in "[]()":
                if ch == '(':
                    stack.append(ch)

                elif ch == '[':
                    stack.append(ch)

                elif ch == ')':
                    if not stack or stack[-1] != '(':
                        boolean = False
                        break
                    stack.pop()

                elif ch == ']':
                    if not stack or stack[-1] != '[':
                        boolean = False
                        break
                    stack.pop()
    
    if boolean and not stack :
        print("yes")
    else :
        print("no")