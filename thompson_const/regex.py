#! usr/bin/env python3
#Arnas Steponavicius
#Adapted from Ian McLoughlin

from state import State
from fragment import Fragment
from shunting import shunt

def compile(infix):
    postfix = shunt(infix)
    postfix = list(postfix)[::-1]

    # Keep track of fragments
    nfa_stack = []

    while postfix:
    	cChar = postfix.pop()

    	if cChar == '.':
    		# Pop two Fragments
    		frag1, frag2 = nfa_stack.pop(), nfa_stack.pop()

    		# Point frag2 accept state at frag1 start state
    		frag2.accept.edges.append(frag1.start)

    		# New instance of fragment to rep new NFA
    		newFrag = Fragment(frag2.start, frag1.accept)

    	elif cChar == '|':
    		# Pop two Fragments
    		frag1, frag2 = nfa_stack.pop(), nfa_stack.pop()

    		# Create new start and accept states
    		accept, start = State(), State(edges=[frag1.start, frag2.start])

    		# Point old accept state to new one
    		frag2.accept.edges.append(accept)
    		frag1.accept.edges.append(accept)

    		# New instance of fragment to rep new NFA
    		newFrag = Fragment(start, accept)

    	elif cChar == '*':
    		# Pop one fragment
    		frag = nfa_stack.pop()

    		# Create new start and accept states
    		accept, start = State(), State(edges=[frag.start, accept])

    		# Point arrows
    		frag.accept.edges.extend([frag.start, accept])

    		# New instance of fragment to rep new NFA
    		newFrag = Fragment(start, accept)
    	else:
    		accept = State()
    		start = State(label=cChar, edges=[accept])
    		newFrag = Fragment(start, accept)

    	nfa_stack.append(newFrag)
    # The NFA stack should have exactly 1 NFA
    return nfa_stack.pop()

def followes(state, current):
	# Only do this when we haven't seen the state.
	if state not in current:
		# Put the state itself into current
		current.add(state)
		# See whether state is labelled by e(psilon)
		if state.label is None:
			#Loop through states pointed to by this one
			for x in state.edges:
				# Follow all of their e(psilons)
				followes(x, current)

def match(regex, s):
    # This function will return true if the regular expression
    # regex fully matches the string s. It returns false otherwise

    # Compile the regular expression into an NFA
    nfa = compile(regex)

    # Try to match the regex to the string s
    # Current set of states
    current = set()
    followes(nfa.start, current)
    prev = set()

    # Loop through chars in s
    for cChar in s:
    	# Keep track of where we are, create new empty set for next state
    	prev, current = current, set()
    	
    	# Loop through previous states
    	for state in prev:
    		# Only follow arrows not labeled by e(psilon).
    		if state.label is not None:
    			if state.label == cChar:
    				# Append the state(s) at the end of the arrow to current
    				followes(state.edges[0], current)

    # Ask the NFA if it matches the string s
    return (nfa.accept in current)

print(match("a.b|b*", "cbbbbbbbb"))