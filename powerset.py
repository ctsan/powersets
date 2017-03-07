#!/usr/bin/env python
from itertools import combinations
from sys import argv

def set_printer(name,s):
        l = list(s)
        print(name, " = " ,sorted(l, key=len))

initial_set = set(argv[1:])
final_set = set()


for i in range( len(initial_set) + 1 ):
        final_set |= set ( combinations( initial_set, i) )

set_printer("S",initial_set)
set_printer("P(S)",final_set)
