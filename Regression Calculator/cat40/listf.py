''''
returns a tuple of entry number, greatest value
'''
def greatest(a):
    b = list(a)
    b.sort()
    return a.index(b[-1]),b[-1]

'''
Returns a tuple of entry number, lowest value.
'''
def least(a):
    b = list(a)
    b.sort()
    return a.index(b[0]),b[0]

'''
Returns a list of equivalent values in two lists.
'''
def compare(a,b):
    return list(set(a)&set(b))

'''
Checks for duplicates in a list. Returns true if duplicates.
'''
def checkduplicate(a):
    return list(set(a))!=a

'''
Checks for duplicates in a list and returns a list with no duplicates
'''
def delduplicate(a):
    return list(set(a))
'''
Returns a list cut down to a specified length.
'''
def truncate(a, length):
    return [a[i] for i in range(length)]

'''
Picks a random value from a list.
'''
import random
def pick(l):
    return l[random.randint(0, len(l)-1)]


'''
searches a list for a value, returns the index number(s)
'''
def find(val, l):
    found = []
    for i, thing in enumerate(l):
        if val == thing:
            found.append(i)
    return found

'''
flattens a list of lists
List can be irregular ([a, b, c], [e, f, g, h, i], j, k, l])
'''
def flatten(l):
    import collections
    newl = []
    for thing in l:
        if isinstance(thing, collections.Iterable) and not isinstance(thing, (str, bytes)):
            for item in genflatten(thing):
                newl.append(item)
        else:
            newl.append(thing)
    return newl

'''
like flatten, but a generator
'''
def genflatten(l):
    import collections
    for thing in l:
        if isinstance(thing, collections.Iterable) and not isinstance(thing, (str, bytes)):
            for item in genflatten(thing):
                yield item
        else:
            yield thing

'''
class for dealing with strings in lists
'''
class string(object):
    @classmethod
    def __init__(self):
        None
        
    '''
    takes a list of strings and merges the strings between two charecters
    '''
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

    '''
    splits a string into lists
    like string.split(), but will add the split charecter into the list
    Note: use str.partition() for single splits
    '''
    @classmethod
    def split(self, s, char):
        l = s.split(char)
        for i, thing in enumerate(l):
            l[i] = [thing, char]
        flatten(l)
        del l[len(l)-1]
        return l      
