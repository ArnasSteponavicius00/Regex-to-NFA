#! usr/bin/env python3
#Arnas Steponavicius
#Classes used in Thompson's construction, adapted from Ian McLoughlin

class State:
    #Every state has 0, 1, or 2 edges from it.
    edges = []

    #Label for arrows, None means epsilon
    label = None

    # Constructor for Class.
    def __init__(self, label = None, edges = []):
       self.edges = edges
       self.label = label

    

