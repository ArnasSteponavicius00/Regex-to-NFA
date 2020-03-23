#! usr/bin/env python3
#Arnas Steponavicius
#Adapted from Ian McLoughlin

from state import State
from fragment import Fragment
from shunting import shunt


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