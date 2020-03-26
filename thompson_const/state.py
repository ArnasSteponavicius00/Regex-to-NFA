#! usr/bin/env python3
#Arnas Steponavicius
#Classes used in Thompson's construction, adapted from Ian McLoughlin

class State:
    """A State with one or two edges, all edges are labelled by label"""
    def __init__(self, label = None, edges = []):
        #Every state has 0, 1, or 2 edges from it.
        self.edges = edges if edges else []
        #Label for arrows, None means epsilon
        self.label = label