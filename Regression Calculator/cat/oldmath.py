# Class for math computations

# Determines number of decimal places a number has.
def decimalplaces(num):
    return len(str(round(num%1,15)))

# Takes the root of a number with a given base.
# Returns numerical value.
# Use newmath.root() for display strings.
def root(n, base=2):
    return n**(1.0/base)

# Returns true if input is integer, false if not.
def isint(num):
    return num%1==0

# Returns true of input is close to an integer (within defined range).
def closeint(num, r=.05):
    return abs(round(num)-num)<=r 

# Compares to list of known fractions.
# Returns true if in it.
def isfrac(num, fracs=[float(x)/y for y in [9,16] for x in range(1,y)]):
    return num in fracs
