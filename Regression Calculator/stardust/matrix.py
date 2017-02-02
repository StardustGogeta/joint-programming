from copy import deepcopy

# Display matrices nicely.
def disp(a): # Displays the matrix as a 2D array.
    return str(a)[1:-1].replace('], ',']\n')
def flat(a): # Flattens the matrix into a single list.
    return [A for b in a for A in b]
    
# Creating new matrices.
def zero(x,y): # Creates a matrix of only zeros with given dimensions.
    return [[0 for b in range(y)] for a in range(x)]
def ident(x): # Creates a square identity matrix of the given order.
    A = zero(x,x)
    for a in range(x):
        A[a][a] = 1
    return A
def new(x,y): # Creates a matrix of the given dimensions with values corresponding to position.
    return [[b for b in range(y)] for a in range(x)]
def fill(x,y,z): # Creates a matrix with given dimensions, filled with one number.
    return [[z for b in range(y)] for a in range(x)]

# Manipulating existing matrices.
def add(a,b): # Adds two matrices of the same dimensions.
    assert (len(a),len(a[0]))==(len(b),len(b[0])), "The matrices are not of the same dimensions."
    return [[a[x][y]+b[x][y] for y in range(len(a))] for x in range(len(a[0]))]
def sub(a,b): # Subtracts two matrices of the same dimensions.
    assert (len(a),len(a[0]))==(len(b),len(b[0])), "The matrices are not of the same dimensions."
    return [[a[x][y]-b[x][y] for y in range(len(a))] for x in range(len(a[0]))]
def scale(a,s): # Scales every element of a matrix by a factor.
    return [[a[x][y]*s for y in range(len(a))] for x in range(len(a[0]))]
def mult(a,b): # Multiplies two matrices of the correct dimensions.
    assert len(a[0])==len(b), "The matrices are not of the correct dimensions."
    return [[sum([e*f for e,f in zip(a[x],[b[A][y] for A in range(len(b))])]) for y in range(len(b[0]))] for x in range(len(a))]
def trans(a): # Transposes a given matrix.
    return [[a[y][x] for y in range(len(a))] for x in range(len(a[0]))]
def coftr(a): # Creates the matrix of cofactors.
    return [[a[x][y]*(-1)**(x+y) for y in range(len(a))] for x in range(len(a[0]))]
def adj(a): # Creates the adjoint matrix of the input.
    return [[a[y][x]*(-1)**(x+y) for y in range(len(a))] for x in range(len(a[0]))]
def det(a): # Finds the determinant of a square matrix.
    if len(a)==2:
        return a[0][0]*a[1][1]-a[0][1]*a[1][0]
    c = 0
    for y in range(len(a[0])):
        b = deepcopy(a)
        b.pop(0)
        for X in b:
            X.pop(y)
        c += a[0][y]*det(b)*((y%2)*-2+1)
    return c
def minors(a): # Calculates the matrix of minors.
    c = new(len(a),len(a[0]))
    for x in range(len(a)):
        for y in range(len(a[0])):
            b = deepcopy(a)
            b.pop(x)
            for X in b:
                X.pop(y)
            c[x][y]=det(b)
    return c
def inv(a): # Calculates the inverse of a given matrix.
    return scale(adj(minors(a)),1/det(a))

