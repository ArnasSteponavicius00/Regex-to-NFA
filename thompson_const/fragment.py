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

#Create an instance of the Class
instance = State(label = 'a', edges = [])

#Different instance of the Class that contains instance
othInstance = State(edges = [instance])

print(instance.label)
#Print reference for edges of instance
print(othInstance.edges[0])

fragment = Fragment(instance, othInstance)
print(fragment)


