import stardust
import cat
import sys
import sympy
from itertools import product
def fit(attempt):
    fitness = 0
    try:
        fitness += sum((1 if ys[xs.index(x)] == eval(attempt) else 0) for x in xs)
        return fitness
    except:
        return 0

def checkmatch():
    if input('does this match your equation? (y/n)\n').lower() == 'y':
        sys.exit()
    else:
        return False

def getnum(string=''):     
    while True:
        try: n = eval(input(string))
        except (SyntaxError, NameError, ZeroDivisionError) as e:
            cat.error.error(str(e))
            print('please try again')
            pass
        else: return n

def comb(r):
    if r == 0:
        yield nums
    else:
        for e in product(nums, ops, repeat=r):
            s = ''
            for p in e:
                s += str(p)
            #extra step to end with number instead of operator
            for newe in product([s], nums):
                yield ''.join(newe)
        
xs = input('enter input points, seperated by commas\n').replace(' ', '').split(',')
ys = input('enter output points, seperated by commas\n').replace(' ', '').split(',')
xs = [eval(x) for x in xs]
ys = [eval(y) for y in ys]
found = []
r = cat.newmath.regression(xs, ys)
print(r.standreg())
checkmatch()
print(r.expreg())
checkmatch()
print(r.rootreg())
checkmatch()
print(r.sinreg())
checkmatch()

complexitylimit = getnum('input complexity limit\n')
#use stardust method <=4, then cat method (4 seems to be where
#efficencies intersect)
complexity = 1
fitness, bestFit, indices = 0,0,[0]
chars = "x-0123456789%+*/()."
x = sympy.Symbol('x')
addLen = (len(chars))
while complexity <= 4 and complexity <= complexitylimit:
    attempt = ''
    for a in indices:
        attempt += chars[a]
    fitness = fit(attempt)
    try: attempt = sympy.simplify(attempt)
    except: pass
    if bestFit < fitness and attempt not in found:
        bestFit = fitness
        print("\t{0} received a fitness of {1}.\n".format(attempt,fitness))
        checkmatch()
    found.append(attempt)
    indices[-1] += 1
    addLen -= 1 if addLen else -1*(len(chars))**len(attempt)
    if not addLen:
        complexity += 1
        indices = [0] * complexity
        print("\nExtending the attempt to {0} characters.\n".format(len(indices)))
        complexity += 1
    for a in range(len(indices)-1,-1,-1):
        if indices[a] == len(chars):
            indices[a-1] += 1
            indices[a] = 0
            
nums = ['x']+[str(float(a+b)) for a, b in product(list('0123456789'), repeat=2)]
for i, n in enumerate(nums):
    nums[i] = n.lstrip('0')
ops = ['+', '/', '-', '*', '**', '%', '+(', '-(', '*(', '/(', '%(' '**(', ')-', ')+', ')-', ')*', ')/', ')**', ')%']
complexity = 1
running = True
while complexity <= complexitylimit and running:
        for eq in comb(complexity):
            running = False
            for x, y in zip(xs, ys):
                try: z = eval(eq)
                except:
                    running = True
                    pass
                else:
                    if z != y:
                        running = True
                        break
            if not running:
                print('your equation is\n %s' % eq)
        complexity += 1
print('no equation found')
input('press ENTER to exit')
sys.exit()
