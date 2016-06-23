import numpy
import math
import sys
from itertools import product
import newmath

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
                 
xs = input("What is the input number set, separated with commaspaces?\n").split(', ')
ys = input("What is the output number set, separated with commaspaces?\n").split(', ')
xs = [eval(x) for x in xs]
ys = [eval(y) for y in ys]

nums = ['x']+[str(float(a+b)) for a, b in product(list('0123456789'), repeat=2)]
for i, n in enumerate(nums):
    nums[i] = n.lstrip('0')
ops = ['+', '/', '-', '*', '**', '%', '+(', '-(', '*(', '/(', '%(' '**(', ')-', ')+', ')-', ')*', ')/', ')**', ')%']

print(newmath.regression.standreg(xs, ys))
if input('does this match your equation? (y/n)\n').lower() != 'y':
    print(newmath.regression.rootreg(xs, ys))
    if input('does this match your equation (y/n)\n').lower() != 'y':
        print(newmath.regression.sinreg(xs, ys))
        if input('does this match your equation (y/n)\n').lower() != 'y':
            limit = newmath.getnum('input complexity limit')
            print('recomputing. this may take a while.')
            running = True
            reps = 0
            while running and reps <= limit:
                print(reps)
                for eq in comb(reps):
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
                        if input('Does this make sense? (y/n)\n').lower != 'y':
                                running = True
                        else:
                            running = False
                            break
                reps += 1
input('press ENTER to close')
sys.exit()
