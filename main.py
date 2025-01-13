import sys

from ge import GE

_, a, b = sys.argv

result = GE(a, b)

if result:
    print('%s is greater or equal to %s' %(a, b))
else:
    print('%s is less than %s' %(a, b))