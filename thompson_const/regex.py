#! usr/bin/env python3
#Arnas Steponavicius
#Adapted from Ian McLoughlin

from state import State
from fragment import Fragment
from shunting import shunt

def compile(infix):
    """Return NFA fragment of the infix expression"""
    # Convert infix to postfix
    postfix = shunt(infix)
    # Make postfix a stack
    postfix = list(postfix)[::-1]

    # Stac to keep track of fragments
    nfa_stack = []

    while postfix:
        cChar = postfix.pop()

        if cChar == '.':
            # Pop two Fragments
            frag1, frag2 = nfa_stack.pop(), nfa_stack.pop()

            # Point frag2 accept state at frag1 start state
            frag2.accept.edges.append(frag1.start)

            start, accept = frag2.start, frag1.accept

        elif cChar == '|':
            # Pop two Fragments
            frag1, frag2 = nfa_stack.pop(), nfa_stack.pop()

            # Create new start and accept states
            accept, start = State(), State(edges=[frag1.start, frag2.start])

            # Point old accept state to new one
            frag2.accept.edges.append(accept)
            frag1.accept.edges.append(accept)

        elif cChar == '?':
            # Pop one fragment
            frag = nfa_stack.pop()

            # Create new start and accept states
            accept, start = State(), State(edges=[frag.start, accept])

            # Point old accept state to new accept state
            frag.accept.edges.append(accept)

        elif cChar == '+':
            # Pop one fragment
            frag = nfa_stack.pop()

            # Create new start and accept states
            accept, start = State(), State(edges=[frag.start])

            # Point old accept state at the new one
            frag.accept.edges = [frag.start, accept]

        elif cChar == '*':
            # Pop one fragment
            frag = nfa_stack.pop()

            # Create new start and accept states
            accept, start = State(), State(edges=[frag.start, accept])

            # Point arrows
            frag.accept.edges.extend([frag.start, accept])

        else:
            # Create new start and accept states
            accept = State()
            start = State(label=cChar, edges=[accept])

        # New instance of fragment represents NFA
        newFrag = Fragment(start, accept)

        nfa_stack.append(newFrag)

    # The NFA stack should have exactly 1 NFA
    return nfa_stack.pop()