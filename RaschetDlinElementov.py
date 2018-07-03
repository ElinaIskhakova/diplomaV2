import sys
from math import *

def e2_1(Ln,h1,ht,l1):
    return (round(ceil(Ln-h1-ht)/10)*10-l1)

print(e2_1(3800,75,24.950,1600))
