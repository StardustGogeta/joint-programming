NUMPY = 0
try:
    from numpy import polyfit
    NUMPY = 1
except:
    import matrix

def poly(x,y):
    if NUMPY:
        c = [str(x) for x in polyfit(x,y,len(x)-1)]
    else:
        a = [[a**b for b in range(len(x)-1,-1,-1)] for a in x]
        b = [[t] for t in y]
        c = [str(round(A,14)) for B in matrix.mult(matrix.inv(a),b) for A in B]
    return ' + '.join([X for X in (c[A]+'x'+''.join([['⁰','¹','²','³','⁴','⁵','⁶','⁷','⁸','⁹'][int(y)] for y in str(len(c)-int(A)-1)]) if float(c[A])!=0 else '' for A in range(len(c))) if X])
