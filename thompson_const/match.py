#! usr/bin/env python3
#Arnas Steponavicius
#Adapted from Ian McLoughlin

from regex import compile

def followes(state, current):
    """Follows edges labelled as e(psilon)
    :param state: object
    :param current: object
    """
    # Only do this when we haven't seen the state.
    if state not in current:
        # Put the state itself into current
        current.add(state)
        print(current)
        # See whether state is labelled by e(psilon)
        if state.label is None:
            #Loop through states pointed to by this one
            for x in state.edges:
                # Follow all of their e(psilons)
                followes(x, current)

def match(regex, s):
    """This function will return true if the regular expression
    fully matches the string s. It returns false otherwise
    :param regex: string
    :param s: string
    :return: whether nfa matches string
    """

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