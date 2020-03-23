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