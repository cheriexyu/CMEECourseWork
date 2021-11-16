#!/usr/bin/env python3
#############################
# Quick profiling with timeit 
#############################
#Loop vs list comprehensions: which is faster?

iters=1000000

import timeit

from profileme import my_squares as my_squares_loops #importing functions from other scripts 
from profileme2 import my_squares as my_squares_lc

#loops vs the join method for strings: which is faster?

mystring = "my string"

from profileme import my_join as my_join_join
from profileme2 import my_join as my_join 

#Using time
import time
start = time.time()
my_squares_loops(iters)
print("my_squares_loops takes %f s to run." % (time.time() - start)) #if you run this many times, the answer is different each time 

start = time.time()
my_squares_lc(iters)
print("my_squares_lc takes %f s to run." % (time.time() - start))