import sys

from ge import GE

_, a, b = sys.argv

result = GE(a, b)

print("%s %s %s" %(a, '>=' if result else '<' ,b))