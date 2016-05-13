import numpy as np
import matplotlib.pyplot as plt

import newton

def f(x):
  return x**3 - x + np.sqrt(2.)/2.
  
def f_pr(x):
  return 3*x**2 -1
  
  
try:
  x = newton.method(f, f_pr, -1., 0.0001)
  print "final value:", x 
except ZeroDivisionError:
	print "Oops, divided by zero."
	print "Try again with different initial guess."
