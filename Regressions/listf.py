# Returns a tuple of entry number, greatest value
def greatest(List):
    High = List[0]
    for i, v in enumerate(List):
        if v >= High:
            High = v
            HighNum = i
    return HighNum, High

#Returns a tuple of entry number, lowest value
def least(List):
    Low = List[0]
    for i, v in enumerate(List):
        if v <= Low:
            Low = v
            LowNum = i
    return LowNum, Low

#Returns a list of equavilent values in a two lists
def compare(List1, List2):
    a = 0
    Values = []
    for value in List1:
        if value in List2:
            Values.append(value)
    return Values

#Checks for duplicates in a list. Returns true if duplicates. 
def checkduplicate(List):
    from copy import copy
    Err = False
    Entry = 0
    for values in List:
        List2 = copy(List)
        del List2[Entry]
        if List[Entry] in List2:
            Err = True
        Entry = Entry + 1
    return Err

#Checks for duplicates in a list and returns a list with no duplicates
def delduplicate(list1):
    from copy import copy
    a = 0
    list3 = []
    for value in List:
        list2 = copy(list1)
        del list2[a]
        if value in list2:
            list3.append((a, value))
    return list3

'''
Cuts a list down to a specified lenth.
'''
def truncate(list1, lenth):
    for i in range(lenth, len(list1)):
        del list1[i]

'''
Picks a random value from the list
'''
def pick(l):
    import random
    return l[random.randint(0, len(l)-1)]

def find(val, l):
    for thing in l:
        if val in thing:
            return thing
    raise IndexError('No matching values')
