#! usr/bin/env python3
#Arnas Steponavicius
#NFA Fragment adapted from Ian McLoughlin

from state import State

class Fragment:
    #Start state
    start = None
    #Accept State
    accept = None

    def __init__(self, start, accept):
        self.start = start
        self.accept = accept

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

def regex_compile(infix):
    postfix = shunt(infix)
    postfix = list(postfix)[::-1]

    # Keep track of fragments
    nfa_stack = []

    while postfix:
    	cChar = postfix.pop()

    	if cChar == '.':
    		# Pop two Fragments
    		frag1 = nfa_stack.pop()
    		frag2 = nfa_stack.pop()

    		# Point frag2 accept state at frag1 start state
    		frag2.start.edges.append(frag1.start)

    		# New instance of fragment to rep new NFA
    		newFrag = Fragment(frag2.start, frag1.accept)

    	elif cChar == '|':
    		# Pop two Fragments
    		frag1 = nfa_stack.pop()
    		frag2 = nfa_stack.pop()

    		# Create new start and accept states
    		accept = State()
    		start = State(edges=[frag1.start, frag2.start])

    		# Point old accept state to new one
    		frag2.start.edges.append(accept)
    		frag1.start.edges.append(accept)

    		# New instance of fragment to rep new NFA
    		newFrag = Fragment(start, accept)

    	elif cChar == '*':
    		# Pop one fragment
    		frag = nfa_stack.pop()

    		# Create new start and accept states
    		accept = State()
    		start = State(edges=[frag.start, accept])

    		# Point arrows
    		frag.accept.edges.extend([frag.start, accept])

    		# New instance of fragment to rep new NFA
    		newFrag = Fragment(start, accept)
    	else:
    		accept = State()
    		start = State(label=cChar, edges=[accept])
    		newFrag = Fragment(start, accept)

    	nfa_stack.append(newFrag)
    # The NFA stack should have exactky 1 nfa
    return nfa_stack.pop()



def match(regex, s):
    # This function will return true if the regular expression
    # regex fully matches the string s. It returns false otherwise

    # Compile the regular expression into an NFA
    nfa = regex_compile(regex)
    # Ask the NFA if it matches the string s
    return nfa

print(match("(a.b)|c*", "bbbbbbbbbb"))

