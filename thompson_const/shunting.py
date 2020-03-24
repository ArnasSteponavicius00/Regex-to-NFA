#! usr/bin/env python3

#Arnas Steponavicius.
#Shunting yard algorithm for regular expressions.
#Adapted from Ian McLoughlin 

def shunt(infix):
    infix = list(infix)[::-1]
    print(f"\nREVERSED INFIX: {infix}")
    # Operator stack, Output list
    opstack, postfix = [], []
    
    # Operator precedence.
    precedence = {'*': 100, '.': 80, '|': 60, ')': 40, '(': 20}

    #Loop through input one at a time

    '''
    Walrus Operator attempt kept returning an error of "IndexError: pop from empty list", 
    Reference: https://www.youtube.com/watch?v=XLIHPU_jxUY
    while (cChar := infix.pop()):
    '''
    print("\nINFIX LIST STACK:")
    while infix:
        # Pop a character from the input
        print(infix)
        cChar = infix.pop()

        # Decide what to do based on the character
        if cChar == '(':
            # Push and open to the opstack stack
            opstack.append(cChar)

        elif cChar == ')':
            # Pop the operator stack until you find an opening bracket
            while opstack[-1] != '(':
                postfix.append(opstack.pop())
            # Get rid of the opening bracket
            opstack.pop()

        elif cChar in precedence:
            # Push any operators on the opstack stack with higher precedence to the output
            while opstack and precedence[cChar] < precedence[opstack [-1]]:
                postfix.append(opstack.pop())
            # Push cChar to the operator stack
            opstack.append(cChar)

        else:
            # Generally just push the character to the output.
            postfix.append(cChar)

    # Pop all operators to the output
    while opstack:
        postfix.append(opstack.pop())


    # Convert output list to String
    return ''.join(postfix)
