import itertools

def foo(l):
     yield from itertools.product(*([l] * 4)) 

for x in foo('adancewithdiana'):
     print(''.join(x))
