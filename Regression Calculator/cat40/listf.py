import random
import collections
#returns a tuple of entry number, greatest value
def greatest(a):
    b = list(a)
    b.sort()
    return a.index(b[-1]),b[-1]


#Returns a tuple of entry number, lowest value.
def least(a):
    b = list(a)
    b.sort()
    return a.index(b[0]),b[0]

#Returns a list of equivalent values in two lists.
def compare(a,b):
    return list(set(a)&set(b))

#Checks for duplicates in a list. Returns true if duplicates.
def checkduplicate(a):
    return list(set(a))!=a

#Checks for duplicates in a list and returns a list with no duplicates
def delduplicate(a):
    return list(set(a))

#Returns a list cut down to a specified length.
def truncate(a, length):
    return [a[i] for i in range(length)]

#Picks a random value from a list.
def pick(l):
    return l[random.randint(0, len(l)-1)]

#searches a list for a value, returns the index number(s)
def find(val, l):
    found = []
    for i, thing in enumerate(l):
        if val == thing:
            found.append(i)
    return found

#flattens a list of lists
#List can be irregular ([[a, b, c], [e, f, g, h, i], j, k, l])
def flatten(l):
    l = [a if isinstance(a, collections.Iterable) else [a] for a in l]
    l = [a for b in l for a in b]
    for thing in l:
        if isinstance(thing, collections.Iterable) and not isinstance(thing, (str, bytes)):
            l = flatten(l)
    return l

#like flatten, but a generator
def genflatten(l):
    for thing in l:
        if isinstance(thing, collections.Iterable) and not isinstance(thing, (str, bytes)):
            for item in genflatten(thing):
                yield item
        else:
            yield thing

#strips an entry from a list
def strip(v, l):
    newl = []
    for i in l:
        if i != v:
            newl.append(i)
    return newl

#strips an entry from right
def rstrip(v, l):
    strip = False
    for i, value in enumerate(reversed(l)):
        if value != v:
            break
    i = len(l) - i
    return l[:i]

#strips an entry from left
def lstrip(v, l):
    strip = False
    for i, value in enumerate(l):
        if value != v:
            break
    i = len(l) - i
    return l[:i]


#class for dealing with strings in lists
class string(object):
    @classmethod
    def __init__(self):
        None
        
    #takes a list of strings and merges the strings between two charecters
    @classmethod
    def merge(self, l, start, end=None):
        if end is None:
            end = start
        newl = []
        startmerge = False
        for char in l:
            if char == end:
                newl.append(''.join([start]+newl2+[end]))
                startmerge = False
            elif char == start:
                newl2 = []
                startmerge = True
            if startmerge and char != start:
                newl2.append(char)
            elif char != end and char != start:
                newl.append(char)
        return newl

    #splits a string into lists
    #like string.split(), but will add the split charecter into the list
    #Note: use str.partition() for single splits
    @classmethod
    def split(self, s, char):
        l = s.split(char)
        for i, thing in enumerate(l):
            l[i] = [thing, char]
        flatten(l)
        del l[len(l)-1]
        return l      
