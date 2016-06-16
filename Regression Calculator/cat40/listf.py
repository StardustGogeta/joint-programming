# Returns a tuple of entry number, greatest value.
def greatest(a):
    b = list(a)
    b.sort()
    return a.index(b[-1]),b[-1]

# Returns a tuple of entry number, lowest value.
def least(a):
    b = list(a)
    b.sort()
    return a.index(b[0]),b[0]

# Returns a list of equivalent values in two lists.
def compare(a,b):
    return list(set(a)&set(b))

# Checks for duplicates in a list. Returns true if duplicates.
def checkduplicate(a):
    return list(set(a))!=a

# Checks for duplicates in a list and returns a list with no duplicates
def delduplicate(a):
    return list(set(a))

# Returns a list cut down to a specified length.
def truncate(a, length):
    return [a[i] for i in range(length)]

# Picks a random value from a list.
import random
def pick(l):
    return l[random.randint(0, len(l)-1)]

# Finds the first subset of a list that contains a value.
def find(v, l):
    return [x for x in l if v in x][0]
    raise IndexError('No matching values')
