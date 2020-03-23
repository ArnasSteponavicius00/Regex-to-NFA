#! usr/bin/env python3

#Arnas Steponavicius.
#Shunting yard algorithm for regular expressions.

def shunt(infix):
    infix = list(infix)[::-1] # reverse list.
    print(f"\nENTERED INFIX: {infix}\n")
    #Operator stack.
    opstack, postfix = [], []

    #Operator precedence.
    precedence = {'*': 100, '.': 80, '|': 60,')': 40 ,'(': 20}

    #Loop through input one at at time (Try walrus operator)
    while infix:
        #Pop character from input.
        cChar = infix.pop()

        #Decide what to do based on character.
        if cChar == '(':
            #Push to stack
            opstack.append(cChar)


        elif cChar == ')':
            #Pop the operator stack until you find opening bracket
            while opstack[-1] != '(':
                postfix.append(opstack.pop())
            #Get rid of the opening bracket
            opstack.pop()

        elif cChar in precedence:
            while opstack and precedence[cChar] < precedence[opstack[-1]]:
                postfix.append(opstack.append(cChar))
            #Push cChar to operator stack
            opstack.append(cChar)

        else:
            #Generally just push the character to the output
            postfix.append(cChar)

    while opstack:
        postfix.append(opstack.pop())

    return ''.join(postfix)

