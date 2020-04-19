testcases = int(input())

for _ in range(testcases):
    expression = input()
    expression = list(expression)
    
    evalstack = list()
    for char in expression:
        if(char == ')'):
            #evaluate stack
            
            # index of last open bracket
            index = 0
            for i in range(len(evalstack)-1 , 0, -1):
                if(evalstack[i] == "("):
                    index = i
                    break
                
            part = evalstack[index+1:]
            evalstack = evalstack[:index]
            part = part[0]+part[2]+part[1]
            evalstack.append(part)
            
        else:
            #push onto the stack
            evalstack.append(char)
            
    print("".join(evalstack))
