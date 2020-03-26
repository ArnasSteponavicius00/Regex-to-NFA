#! usr/bin/env python3
#Arnas Steponavicius
#NFA Fragment adapted from Ian McLoughlin

from state import State

class Fragment:
    """NFA Fragment with a start and accept state"""
    def __init__(self, start, accept):
        #Start state
        self.start = start
        #Accept State
        self.accept = accept