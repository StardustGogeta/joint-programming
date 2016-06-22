import stardust
try: import numpy as np
except ImportError:
    hasnumpy = False
else:
    def mult(a, b):
        return a*b
    def inv(a):
        return a.I
    hasnumpy = True
#keep cat BELOW numpy
import cat
