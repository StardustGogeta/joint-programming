try:
    import numpy as np
except:
    import matrix

def poly(x,y):
    a = [[a**b for b in range(len(x)-1,-1,-1)] for a in x]
    b = [[t] for t in y]
    try:
        a,b = np.matrix(a),np.matrix(b)
        c = a.I*b
        c = [str(round(c[X].A1[0],10)) for X in range(len(x))]
    except ValueError:
        c = [str(round(A,14)) for B in matrix.mult(matrix.inv(a),b) for A in B]
    return ' + '.join([X for X in (c[A]+'x'+''.join([['⁰','¹','²','³','⁴','⁵','⁶','⁷','⁸','⁹'][int(y)] for y in str(len(c)-int(A)-1)]) if float(c[A])!=0 else '' for A in range(len(c))) if X])
