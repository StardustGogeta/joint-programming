'''
class for math computations
'''

'''
Determines number of decimal places a number has
'''
def decimalplaces(num):
    return len(str(num).split('.')[1])

'''
takes the root of a number with a given base
Returns numerical value
Use newmath.root() for display strings
'''
def root(n, base=2):
    p = 1.0/base
    return n**p

'''
Returns true if input is integer, false if not
'''
def isint(num):
    import math
    return int(num) == math.ceil(num)

'''
returns true of input is close to an integer (within defined range)
'''
def closeint(num, r=.05):
    p = decimalplaces(r)
    n = round(num, p)
    i = int(round(num, 0))
    return n <= i+r and num >= i-r

'''
compares to list of known fractions
returns true if in it
'''
def isfrac(num, fracs = [1./16, 2./16, 3./16, 4./16, 5./16, 6./16, 7./16, 8./16,
                         9./16, 10./16, 11./16, 12./16, 13./16, 14./16, 15./16,
                         1./9, 2./9, 3./9, 4./9, 5./9, 6./9, 7./9, 8./9]):
    for i, f in enumerate(fracs):
        fracs[i] = round(f, decimalplaces(num))
    return num in fracs
