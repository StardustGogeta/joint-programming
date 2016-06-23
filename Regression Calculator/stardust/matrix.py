import copy

def flat(a):
    return [A for b in a for A in b]
def disp(a):
    return str(a)[1:-1].replace('], ',']\n')
def new(x,y):
    return [[b for b in range(y)] for a in range(x)]
def mult(a,b):
    return [[sum([e*f for e,f in zip(a[x],[b[A][y] for A in range(len(b))])]) for y in range(len(b[0]))] for x in range(len(a))]
def scale(a,s):
    return [[a[x][y]*s for y in range(len(a))] for x in range(len(a[0]))]
def adj(a):
    return [[a[y][x]*(-1)**(x+y) for y in range(len(a))] for x in range(len(a[0]))]
def det(a):
    if len(a)==2:
        return a[0][0]*a[1][1]-a[0][1]*a[1][0]
    else:
        c = 0
        for y in range(len(a[0])):
            b = copy.deepcopy(a)
            b.pop(0)
            for X in b:
                X.pop(y)
            c += a[0][y]*det(b)*((y%2)*-2+1)
        return c
def minors(a):
    if len(a)==2:
        return [[a[1][1],a[1][0]],[a[0][1],a[0][0]]]
    c = new(len(a),len(a[0]))
    for x in range(len(a)):
        for y in range(len(a[0])):
            b = copy.deepcopy(a)
            b.pop(x)
            for X in b:
                X.pop(y)
            c[x][y]=det(b)
    return c
def inv(a):
    return scale(adj(minors(a)),1/det(a))
def zeros(dims):
    return [[[0]*dims[1]]*dims[0]]
# Added to keep compatability with numpy matrix struture. Does absolutly nothing
def matrix(array):
    return array
