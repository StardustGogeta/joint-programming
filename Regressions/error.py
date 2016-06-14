# -*- coding: cp1252 -*-
import random
import time
import os

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Error.cfg')) as errfile:
    ErrMes = [line.rstrip('\n') for line in errfile] #figure out how to avoid stripping this more than once, to allow message"That does not compute" to be repeated about a dozen times on new lines.
UNumErr = len(ErrMes) - 1
##ErrNum = UNumErr
##ErrMes = [''] * (UNumErr + 1)
##
##for values in ErrMes:
##    ErrMes[ErrNum] = lines[ErrNum + 3]
##    ErrNum = ErrNum - 1
#Functions
def error(UnqErr):
    NumErr = random.randint(0, UNumErr)
    if time.strftime('%d') == '1' and time.strftime('%m') == '4':
        print('April Fools!')
    elif time.strftime('%d') == '25' and time.strftime('%m') == '12':
        print('Merry Christmas')
    elif ErrMes[NumErr] == "YOU DIDN'T SAY THE MAGIC WORD!":
        print('Error...and...')
        time.sleep(.5)
        for __ in range(100):
            print('YOU DIDN\'T SAY THE MAGIC WORD!')
            time.sleep(.1)
        print('')
        print(UnqErr)
    elif ErrMes[NumErr] == 'This progam will self destruct in 5 seconds':
        print('''This program will self destruct in 5 seconds''')
        for i in range(5):
            print(i)
            time.sleep(1)
        print('Maybe six...')
        time.sleep(1)
        print('7?')
        time.sleep(1)
        #sys.exit()
        print(UnqErr)
    else:
        print(ErrMes[NumErr] + ' -- ' + UnqErr)
