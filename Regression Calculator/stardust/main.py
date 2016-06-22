import poly
import time
def fit(attempt):
    fitness = 0
    try:
        fitness += sum((1 if y[x.index(e)] == eval(attempt) else 0) for e in x)
        return fitness
    except:
        return 0

x = input("What is the input number set, separated with spaces?\n").split()
y = input("What is the output number set, separated with spaces?\n").split()
z = input("Extra options? (See source for full list.)\n").split(' ')
# Options:
# 1. Minimum complexity (default is 1)
# 2. Charset used (0: basic, 1: advanced)
# 3. Maximum complexity (default is 6)
#x='1 3 5 7 9 11 13 2 4 6 8 10 12 14'.split()
#y='0 0 0 0 0 0 0 5 -10 398053859 -7 -103454 0 2804'.split()
x, y = [eval(e) for e in x], [eval(e) for e in y]
print('Polynomial Regression:',poly.poly(x,y),'\n')
z[0] = 1 if z[0]=='' else int(z[0])
charsets = ["e-0123456789%+*/().","""e\\0123456789%+-_=/*^,.;!()'{}[]:\""""]
chars = charsets[int(z[1])] if len(z)>1 else charsets[0]
maximum = int(z[2]) if len(z)>2 else 10
fitness, bestFit, indices = 0,0,[0]*z[0]
addLen = (len(chars))**z[0]
while fitness < len(x):
    attempt = ''
    for a in indices:
        attempt += chars[a]
    fitness = fit(attempt)
    if bestFit < fitness:
        bestFit = fitness
        print("    {0} received a fitness of {1}.".format(attempt,fitness))
    indices[-1] += 1
    addLen -= 1 if addLen else -1*(len(chars))**len(attempt)
    if not addLen:
        if maximum:
            indices = [0] * (len(indices)+1)
            maximum -= 1
            print("\nExtending the attempt to {0} characters.\n".format(len(indices)))
        else:
            print("\nThe maximum attempt length has been reached.")
            break
    for a in range(len(indices)-1,-1,-1):
        if indices[a] == len(chars):
            indices[a-1] += 1
            indices[a] = 0
