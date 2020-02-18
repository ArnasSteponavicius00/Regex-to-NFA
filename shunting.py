#! usr/bin/env python3

#Arnas Steponavicius.
#Shunting yard algorithm for regular expressions.

#Input.
infix = input("Enter infix:")
print(f"Input is: {infix}")

#Expected output "ab|c*."

#Convert input to a stack like list.
infix = list(infix)[::-1] # reverse list.
print(infix)
#Operator stack.
opstack = []

#Output list.
postfix = []

#Operator precedence.
precedence = {'*': 100, '.': 80, '|': 60,')': 40 ,'(': 20}

#Loop through input one at at time (Try walrus operator)
while infix:
    #Pop character from input.
    cur = infix.pop()

    #Decide what to do based on character.
    if cur == '(':
        #Push to stack
        opstack.append(cur)
    elif cur == ')':
        #Pop the operator stack until you find opening bracket
        while opstack[-1] != '(':
            postfix.append(opstack.pop())
        #Get rid of the opening bracket
        opstack.pop()
    elif cur in precedence:
        while opstack and precedence[cur] < precedence[opstack[-1]]:
            postfix.append(opstack.append(cur))
        #Push cur to operator stack
        opstack.append(cur)
    else:
        #Generally just push the character to the output
        postfix.append(cur)

while opstack:
    postfix.append(opstack.pop())


#Convert output list to string.
postfix = ''.join(postfix)

#Print result.
print(f"Output is: {postfix}")
