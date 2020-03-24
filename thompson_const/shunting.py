#! usr/bin/env python3

#Arnas Steponavicius.
#Shunting yard algorithm for regular expressions.
#Adapted from Ian McLoughlin 

def shunt(infix):
    print(f"ENTERED INFIX: {infix}")
    infix = list(infix)[::-1] # reverse list.

    print(f"REVERSED INFIX: {infix}\n")
    #Operator stack.
    opstack, postfix = [], []

    #Operator precedence.
    precedence = {'*': 100, '.': 80, '|': 60,')': 40 ,'(': 20}

    #Loop through input one at a time

    '''
    Walrus Operator attempt kept returning an error of "IndexError: pop from empty list", 
    Reference: https://www.youtube.com/watch?v=XLIHPU_jxUY

    while (cChar := infix.pop()):
    '''
    print("INFIX LIST:")
    while infix:
        print(infix)
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