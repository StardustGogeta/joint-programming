import sympy
import numpy
import cat

def standreg(xs, ys, retdeg=False):
    x = sympy.Symbol('x'); y = sympy.Symbol('y')
##    cat.newmath.regression.importnumpy()
    deg = len(xs)-1
    array = numpy.zeros((deg+1, deg+1))
    for i, x in enumerate(xs):
        for i2, __ in enumerate(array[i]):
            array[i][i2] = x**(deg-i2)
    A = numpy.matrix(array)
    array = numpy.zeros((deg+1, 1))
    for i, y in enumerate(ys):
        array[i][0] = y
    X = numpy.matrix(array)
    B = A.I * X
    coeffs = [float(i[0]) for i in B]
    eq = ''
    for i, c in enumerate(coeffs):
        #use for comparison; apparently floats are too imprecise
        cr = round(c, 2)
        if c < 10**-10 and c > -(10**-10):
            c = 0
        if cr == 1:
            #sympy does not simplify 1.0*x
            c = 1
##            eq += 'x**%s+' % (deg-i)
##        elif cr:
        eq += '%s*x**%s+' % (c, deg-i)
        #finds actual degree of equation
        if c == deg:
            deg -= 1
    #formats equation to make more readable
    eq = eq.rstrip('+')
    eq = str(sympy.simplify(eq))
##    eq = eq.replace('+-', '-')
    return 'y='+cat.newmath.equation(eq).format()

print(standreg([1, 2, 3, 4], [1, 4, 9, 16]))
